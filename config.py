#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from dotenv import load_dotenv
load_dotenv()

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId", "")

    # Azure OpenAI
    OPENAI_API_KEY = os.environ.get("OpenAIApiKey", "")
    OPENAI_ENDPOINT = os.environ.get("OpenAIEndpoint", "")
    OPENAI_API_VERSION = os.environ.get("OpenAIApiVersion", "2024-12-01-preview")
    OPENAI_DEPLOYMENT = os.environ.get("OpenAIDeployment", "gpt-4o-mini")