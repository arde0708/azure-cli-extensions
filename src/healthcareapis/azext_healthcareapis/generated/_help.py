# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['healthcareapis service'] = """
    type: group
    short-summary: healthcareapis service
"""

helps['healthcareapis service list'] = """
    type: command
    short-summary: Get all the service instances in a subscription.
    examples:
      - name: List all services in resource group
        text: |-
               az healthcareapis service list --resource-group "rgname"
"""

helps['healthcareapis service show'] = """
    type: command
    short-summary: Get the metadata of a service instance.
    examples:
      - name: Get metadata
        text: |-
               az healthcareapis service show --resource-group "rg1" --resource-name "service1"
"""

helps['healthcareapis service create'] = """
    type: command
    short-summary: Create or update the metadata of a service instance.
    examples:
      - name: Create or Update a service with all parameters
        text: |-
               az healthcareapis service create --resource-group "rg1" --resource-name "service1" --identity type="Syst\
emAssigned" --kind "fhir-R4" --location "westus2" --properties "{\\"accessPolicies\\":[{\\"objectId\\":\\"c487e7d1-3210\
-41a3-8ccc-e9372b78da47\\"},{\\"objectId\\":\\"5b307da8-43d4-492b-8b66-b0294ade872f\\"}],\\"authenticationConfiguration\
\\":{\\"audience\\":\\"https://azurehealthcareapis.com\\",\\"authority\\":\\"https://login.microsoftonline.com/abfde7b2\
-df0f-47e6-aabf-2462b07508dc\\",\\"smartProxyEnabled\\":true},\\"corsConfiguration\\":{\\"allowCredentials\\":false,\\"\
headers\\":[\\"*\\"],\\"maxAge\\":1440,\\"methods\\":[\\"DELETE\\",\\"GET\\",\\"OPTIONS\\",\\"PATCH\\",\\"POST\\",\\"PU\
T\\"],\\"origins\\":[\\"*\\"]},\\"cosmosDbConfiguration\\":{\\"offerThroughput\\":1000},\\"exportConfiguration\\":{\\"s\
torageAccountName\\":\\"existingStorageAccount\\"}}"
      - name: Create or Update a service with minimum parameters
        text: |-
               az healthcareapis service create --resource-group "rg1" --resource-name "service2" --kind "fhir-R4" --lo\
cation "westus2" --properties "{\\"accessPolicies\\":[{\\"objectId\\":\\"c487e7d1-3210-41a3-8ccc-e9372b78da47\\"}]}"
"""

helps['healthcareapis service update'] = """
    type: command
    short-summary: Update the metadata of a service instance.
    examples:
      - name: Patch service
        text: |-
               az healthcareapis service update --resource-group "rg1" --resource-name "service1" --tags tag1="value1" \
tag2="value2"
"""

helps['healthcareapis service delete'] = """
    type: command
    short-summary: Delete a service instance.
    examples:
      - name: Delete service
        text: |-
               az healthcareapis service delete --resource-group "rg1" --resource-name "service1"
"""

helps['healthcareapis operation-result'] = """
    type: group
    short-summary: healthcareapis operation-result
"""

helps['healthcareapis operation-result show'] = """
    type: command
    short-summary: Get the operation result for a long running operation.
    examples:
      - name: Get operation result
        text: |-
               az healthcareapis operation-result show --location-name "westus" --operation-result-id "exampleid"
"""
