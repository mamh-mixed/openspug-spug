/**
 * Copyright (c) OpenSpug Organization. https://github.com/openspug/spug
 * Copyright (c) <spug.dev@gmail.com>
 * Released under the AGPL-3.0 License.
 */
import React from 'react';
import { Avatar } from 'antd';
import iconSSHExec from './assets/icon_ssh_exec.png';
import iconBuild from './assets/icon_build.png';
import iconParameter from './assets/icon_parameter.png';
import iconDataTransfer from './assets/icon_data_transfer.png';
import iconDataUpload from './assets/icon_data_upload.png';
import iconPushSpug from './assets/icon_push_spug.png';
import iconPushDD from './assets/icon_push_dd.png';
import iconSelect from './assets/icon_select.png';

function Icon(props) {
  switch (props.module) {
    case 'ssh_exec':
      return <Avatar size={props.size || 42} src={iconSSHExec}/>
    case 'build':
      return <Avatar size={props.size || 42} src={iconBuild}/>
    case 'parameter':
      return <Avatar size={props.size || 42} src={iconParameter}/>
    case 'data_transfer':
      return <Avatar size={props.size || 42} src={iconDataTransfer}/>
    case 'data_upload':
      return <Avatar size={props.size || 42} src={iconDataUpload}/>
    case 'push_spug':
      return <Avatar size={props.size || 42} src={iconPushSpug}/>
    case 'push_dd':
      return <Avatar size={props.size || 42} src={iconPushDD}/>
    case undefined:
      return <Avatar size={props.size || 42} src={iconSelect}/>
    default:
      return <Avatar size={props.size || 42}/>
  }
}

export default Icon