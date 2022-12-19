import React, {useEffect, useState} from 'react';
import User from "../actions/user";
import {useLocation, useNavigate, useParams} from "react-router-dom";

import { Auth } from "aws-amplify";
import ItemAmend from "../components/ItemAmend";
import {
  capitalize,
  exportTable,
  getChanges
} from '../resources/main.js'

import {
  SpaceBetween,
  StatusIndicator
} from '@awsui/components-react';


import ApplicationView from '../components/ApplicationView.jsx'
import { useMFApps } from "../actions/ApplicationsHook";
import { useGetServers } from "../actions/ServersHook.js";
import { useMFWaves } from "../actions/WavesHook.js";
import ItemTable from '../components/ItemTable.jsx';
import { useModal } from '../actions/Modal.js';
import {parsePUTResponseErrors} from "../resources/recordFunctions";

const AppTable = (props) => {
  let location = useLocation()
  let navigate = useNavigate();
  let params = useParams();
  //Data items for viewer and table.
  //Main table content hook. When duplicating just create a new hook and change the hook function at the end to populate table.
  const [{ isLoading: isLoadingMain, data: dataMain, error: errorMain }, {update: updateMain, deleteApplications: deleteApp} ] = useMFApps();
  const [{ isLoading: isLoadingServers, data: dataServers, error: errorServers }, {update: updateServers} ] = useGetServers();
  const [{ isLoading: isLoadingWaves, data: dataWaves, error: errorWaves }, { update: updateWaves }] = useMFWaves();

  const dataAll = {application: {data: dataMain, isLoading: isLoadingMain, error: errorMain}, server: {data: dataServers, isLoading: isLoadingServers, error: errorServers}, wave: {data: dataWaves, isLoading: isLoadingWaves, error: errorWaves}};

  //Layout state management.
  const [editingItem, setEditingItem] = useState(false);

  //Main table state management.
  const [selectedItems, setSelectedItems] = useState([]);
  const [focusItem, setFocusItem] = useState([]);

  //Viewer pane state management.
  const [viewerCurrentTab, setViewerCurrentTab] = useState('details');
  const [action, setAction] = useState(['Add']);

  //Get base path from the URL, all actions will use this base path.
  const basePath = location.pathname.split('/').length >= 2 ? '/' + location.pathname.split('/')[1] : '/';
  //Key for main item displayed in table.
  const itemIDKey = 'app_id';
  const schemaName = 'application';

  //Modals
  const { show: showDeleteConfirmaton, hide: hideDeleteConfirmaton, RenderModal: DeleteModal } = useModal()

  function handleNotification(notification)
  {
    return props.updateNotification('add', notification)
  }

  async function handleRefreshClick(e) {
    e.preventDefault();
    await updateMain();
  }

  function handleAddItem()
  {
    navigate({
      pathname: basePath + '/add'
    })
    setAction('Add')
    setFocusItem({});
    setEditingItem(true);

  }

  function handleDownloadItems()
  {
    if (selectedItems.length > 0 ) {
      // Download selected only.
      exportTable(selectedItems, "Applications", "applications")
    } else {
      //Download all.
      exportTable(dataMain, "Applications", "applications")
    }
  }

  function handleEditItem(selection = null)
  {
    if ( selectedItems.length === 1) {
      navigate({
        pathname: basePath + '/edit/' + selectedItems[0][itemIDKey]
      })
      setAction('Edit')
      setFocusItem(selectedItems[0]);
      setEditingItem(true);
    } else if ( selection ) {
      navigate({
        pathname: basePath + '/edit/' + selection[itemIDKey]
      })
      setAction('Edit');
      setFocusItem(selection);
      setEditingItem(true);
    }

  }

  async function handleViewerTabChange(tabselected)
  {
      setViewerCurrentTab(tabselected);
  }

  function handleResetScreen()
  {
    navigate({
      pathname: basePath
    })
    setEditingItem(false);
  }

  function handleItemSelectionChange(selection) {

    setSelectedItems(selection);
    if (selection.length === 1) {

      updateServers(selection[0][itemIDKey]);

    }
    //Reset URL to base table path.
    navigate({
      pathname: basePath
    })

  }

  async function handleSave(editedItem, action) {

    let newApp = Object.assign({}, editedItem);
    try {
      if (action === 'Edit') {
        let app_id = newApp.app_id;
        let app_name = newApp.app_name;
        const session = await Auth.currentSession();
        const apiUser = new User(session);
        newApp = getChanges (newApp, dataMain, itemIDKey);
        delete newApp.app_id;
        var result = await apiUser.putItem(app_id, newApp, schemaName);

        if (result['errors']) {
          console.debug("PUT " + schemaName + " errors");
          console.debug(result['errors']);
          let errorsReturned = parsePUTResponseErrors(result['errors']);
          handleNotification({
            type: 'error',
            dismissible: true,
            header: "Update " + schemaName,
            content: (errorsReturned)
          });
          return false;
        } else {
          handleNotification({
            type: 'success',
            dismissible: true,
            header: "Update " + schemaName,
            content: app_name + " updated successfully.",
          });
          updateMain();
          handleResetScreen();

          //This is needed to ensure the item in selectItems reflects new updates
          setSelectedItems([]);
          setFocusItem({});
        }
      }
      else {

        const session = await Auth.currentSession();
        const apiUser = new User(session);
        delete newApp.app_id;
        var result = await apiUser.postItem(newApp, schemaName);

        if (result['errors']) {
          console.debug("PUT " + schemaName + " errors");
          console.debug(result['errors']);
          let errorsReturned = parsePUTResponseErrors(result['errors']);
          handleNotification({
            type: 'error',
            dismissible: true,
            header: "Add " + schemaName,
            content: (errorsReturned)
          });
          return false;
        } else {
          handleNotification({
            type: 'success',
            dismissible: true,
            header: "Add " + schemaName,
            content: newApp.app_name + " added successfully.",
          });
          updateMain();
          handleResetScreen();
        }
      }
    } catch (e) {
      console.error(e);
      let response = '';
      if ('response' in e && 'data' in e.response) {
        //Check if errors key exists from Lambda errors.
        if (e.response.data.errors)
        {
          response = e.response.data.errors;
        } else if (e.response.data.cause){
          response = e.response.data.cause;
        } else {
          response = 'Unknown error occurred.';
        }
      } else {
        response = 'Unknown error occurred.';
      }

      handleNotification({
        type: 'error',
        dismissible: true,
        header: "Save " + schemaName,
        content: (response)
      });
    }

  }

  function getCurrentApplicationWave() {

    if (selectedItems.length === 1) {
      let waves = dataWaves.filter(function (entry) {
        return entry.wave_id === selectedItems[0].wave_id;
      });

      if ( waves.length === 1){
        return waves[0];
      } else {
        return {};
      }
    }

  }

  async function handleDeleteItemClick(e) {
    e.preventDefault();
    showDeleteConfirmaton();
  }

  async function handleDeleteItem(e) {
    e.preventDefault();
    let currentApp = 0;
    let multiReturnMessage = [];
    let notificationId;

    await hideDeleteConfirmaton();

    //WIP
    //deleteApp(selectedItems);

    try {
      const session = await Auth.currentSession();
      const apiUser = new User(session);
      if(selectedItems.length > 1) {
        notificationId = handleNotification({
          type: 'success',
          loading: true,
          dismissible: false,
          header: "Deleting selected " + schemaName + "s..."
        });
      }

      for(let item in selectedItems) {
        currentApp = item;
        await apiUser.deleteApp(selectedItems[item][itemIDKey]);
        //Combine notifications into a single message if multi selected used, to save user dismiss clicks.
        if(selectedItems.length > 1){
          multiReturnMessage.push(selectedItems[item].app_name);
        } else {
          handleNotification({
            type: 'success',
            dismissible: true,
            header: 'Application deleted successfully',
            content: selectedItems[item].app_name + ' was deleted.'
          });
        }

      }

      //Create notification where multi select was used.
      if(selectedItems.length > 1){
        handleNotification({
          id: notificationId,
          type: 'success',
          dismissible: true,
          header: 'Applications deleted successfully',
          content: multiReturnMessage.join(", ") + ' were deleted.'
        });
      }

      //Unselect applications marked for deletion to clear apps.
      setSelectedItems([]);

      await updateMain();

    } catch (e) {
      console.log(e);
        handleNotification({
            type: 'error',
            dismissible: true,
            header: 'Application deletion failed',
            content: selectedItems[currentApp].app_name + ' failed to delete.'
          });
    }
  }

  const ViewApplication = (props) => {

    const [selectedServers, setSelectedServers] = useState([]);

    if (selectedItems.length === 1) {

      return (
        <ApplicationView {...props}
            app={selectedItems[0]}
            wave={getCurrentApplicationWave()}
            dataAll={dataAll}
            servers={{items: dataServers, isLoading:  isLoadingServers, error: errorServers}}
            handleTabChange={handleViewerTabChange}
            selectedTab={viewerCurrentTab}
          />
      );
    } else {
      return (null);
    }
  }

  useEffect( () => {
    let selected = [];

    if (!isLoadingMain) {

      let item = dataMain.filter(function (entry) {
        return entry[itemIDKey] === params.id;
      });

      if (item.length === 1) {
        selected.push(item[0]);
        handleItemSelectionChange(selected);
        //Check if URL contains edit path and switch to amend component.
        if (location.pathname && location.pathname.match('/edit/')) {
          handleEditItem(item[0]);
        }
      } else if (location.pathname && location.pathname.match('/add')) {
        //Add url used, redirect to add screen.
          handleAddItem();
      }
    }

  }, [dataMain]);

  //Update help tools panel.
  useEffect(() => {
    if (props.schema && props.schema[schemaName].help_content) {
      let tempContent = props.schema[schemaName].help_content;
      tempContent.header = props.schema[schemaName].friendly_name ? props.schema[schemaName].friendly_name : capitalize(schemaName);
      props.setHelpPanelContent(tempContent)
    }
  }, [props.schema]);

  return (
    <div>
    {props.schemaIsLoading ?
      <StatusIndicator type="loading">
        Loading schema...
      </StatusIndicator>
      :
      !editingItem
        ?
        (
          <SpaceBetween direction="vertical" size="xs">
            <ItemTable
              sendNotification={handleNotification}
              schema={props.schema[schemaName]}
              schemaKeyAttribute={itemIDKey}
              schemaName={schemaName}
              dataAll={dataAll}
              items={dataMain}
              selectedItems={selectedItems}
              handleSelectionChange={handleItemSelectionChange}
              isLoading={isLoadingMain}
              errorLoading={errorMain}
              handleRefreshClick={handleRefreshClick}
              handleAddItem={handleAddItem}
              handleDeleteItem={handleDeleteItemClick}
              handleEditItem={handleEditItem}
              handleDownloadItems={handleDownloadItems}
              userAccess={props.userEntityAccess}
              setHelpPanelContent={props.setHelpPanelContent}
              />
            <ViewApplication {...props}
            allData={dataAll}
            />
          </SpaceBetween>
        )
        : <ItemAmend action={action} schemaName={schemaName} schemas={props.schema} userAccess={props.userEntityAccess} item={focusItem} handleSave={handleSave} handleCancel={handleResetScreen} updateNotification={handleNotification} setHelpPanelContent={props.setHelpPanelContent}/>
      }

    <DeleteModal title={'Delete applications'} onConfirmation={handleDeleteItem}>{selectedItems.length === 1 ? <p>Are you sure you wish to delete the selected application?</p> : <p>Are you sure you wish to delete the {selectedItems.length} selected applications?</p>}</DeleteModal>
    </div>
  );
};

export default AppTable;
