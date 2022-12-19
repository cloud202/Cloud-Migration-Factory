import React from 'react';
import { SpaceBetween } from '@awsui/components-react';

// Attribute Display message content
const TextAttribute = (props) => {
  return <div>
    <SpaceBetween size="xxxxs">
      <div>
        <small>{props.name}</small>
      </div>
      <div>
          {typeof props.value === 'string' || props.value instanceof String
          ?
          <strong>{props.value}</strong>
          :
          <strong>{JSON.stringify(props.value)}</strong>
         }
      </div>
    </SpaceBetween>
  </div>;
};

export default TextAttribute;
