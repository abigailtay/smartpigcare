# Data Folder Overview

This folder contains data files used by the SmartPigCare application.

## combined_data.json

- JSON format file containing pig information.
- Each key is a pig ID (e.g., "pig_01").
- Each value is an object with:
  - `feeding`: "yes" or "no"
  - `BCS`: Body Condition Score (integer 1-5)
  - `gait`: Gait status ("normal" or "limping")

This file simulates the combined outputs of the models for demonstration.
