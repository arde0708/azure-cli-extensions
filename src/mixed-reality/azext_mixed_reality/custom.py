# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def list_mixed_reality_operation(cmd, client):
    return client.list()


def check_name_availability_local_mixed_reality(cmd, client,
                                                location,
                                                name,
                                                _type):
    return client.check_name_availability_local(location=location, name=name, type=_type)


def create_mixed_reality_remote_rendering_account(cmd, client,
                                                  resource_group,
                                                  name,
                                                  location,
                                                  tags=None):
    return client.create(resource_group_name=resource_group, account_name=name, tags=tags, location=location)


def update_mixed_reality_remote_rendering_account(cmd, client,
                                                  resource_group,
                                                  name,
                                                  tags=None,
                                                  location=None):
    return client.create(resource_group_name=resource_group, account_name=name, tags=tags, location=location)


def delete_mixed_reality_remote_rendering_account(cmd, client,
                                                  resource_group,
                                                  name):
    return client.delete(resource_group_name=resource_group, account_name=name)


def get_mixed_reality_remote_rendering_account(cmd, client,
                                               resource_group,
                                               name):
    return client.get(resource_group_name=resource_group, account_name=name)


def list_mixed_reality_remote_rendering_account(cmd, client,
                                                resource_group=None):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def regenerate_keys_mixed_reality_remote_rendering_account(cmd, client,
                                                           resource_group,
                                                           name,
                                                           serial=None):
    return client.regenerate_keys(resource_group_name=resource_group, account_name=name, serial=serial)


def get_keys_mixed_reality_remote_rendering_account(cmd, client,
                                                    resource_group,
                                                    name):
    return client.get_keys(resource_group_name=resource_group, account_name=name)


def create_mixed_reality_spatial_anchors_account(cmd, client,
                                                 resource_group,
                                                 name,
                                                 location,
                                                 tags=None):
    return client.create(resource_group_name=resource_group, account_name=name, tags=tags, location=location)


def update_mixed_reality_spatial_anchors_account(cmd, client,
                                                 resource_group,
                                                 name,
                                                 tags=None,
                                                 location=None):
    return client.create(resource_group_name=resource_group, account_name=name, tags=tags, location=location)


def delete_mixed_reality_spatial_anchors_account(cmd, client,
                                                 resource_group,
                                                 name):
    return client.delete(resource_group_name=resource_group, account_name=name)


def get_mixed_reality_spatial_anchors_account(cmd, client,
                                              resource_group,
                                              name):
    return client.get(resource_group_name=resource_group, account_name=name)


def list_mixed_reality_spatial_anchors_account(cmd, client,
                                               resource_group=None):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def regenerate_keys_mixed_reality_spatial_anchors_account(cmd, client,
                                                          resource_group,
                                                          name,
                                                          serial=None):
    return client.regenerate_keys(resource_group_name=resource_group, account_name=name, serial=serial)


def get_keys_mixed_reality_spatial_anchors_account(cmd, client,
                                                   resource_group,
                                                   name):
    return client.get_keys(resource_group_name=resource_group, account_name=name)
