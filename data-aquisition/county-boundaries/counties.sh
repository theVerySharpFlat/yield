#!/bin/bash

curl -LJ "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/us-county-boundaries/exports/csv?lang=en&timezone=America%2FNew_York&use_labels=true&delimiter=%3B" -o counties.csv
