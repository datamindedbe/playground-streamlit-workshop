# 🧑‍💻 Streamlit Workshop 06-11-2025

> [!IMPORTANT]  
> Before running the `shell` commands below, you will need the correct value
> for the `PUBLIC_BUCKET_GOOGLE_KEY` environment variable. We will make its
> value available **at the start of the workshop**. Without it,
> you will **not be able to authenticate** to the used Google Cloud services.

First, export the Application Default Credentials:

```bash
# Set ADC
export PUBLIC_BUCKET_GOOGLE_KEY='...'
```

Then, run the following commands to setup your development environment:

```bash
# Dev environment setup
sh demo-app/scripts/00_setup.sh
cd demo-app

# Running the Streamlit app
sh scripts/01_run.sh
```

After setting up your dev environment, you can restart a stopped application by
running the last command:

```bash
sh scripts/01_run.sh
```

In line with security best practices, access to these credentials will be
**instantly revoked** at the end of the 06-11-2025 workshop.
