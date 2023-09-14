# Databricks notebook source
!pip install tqdm

# COMMAND ----------

from download_dados import ColigacaoDownloader 

cd = ColigacaoDownloader()
cd.download(['2022'])
cd.unzip(['2022'], 'SP')

# COMMAND ----------

import os
import requests

os.getcwd()
