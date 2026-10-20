# Branch Gap Radar Pro — Streamlit

This project hosts the self-contained Branch Gap Radar Pro dashboard through Streamlit's static-file serving. The Streamlit landing page opens the dashboard in a full browser page so Excel uploads and generated report downloads work without iframe restrictions.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Community Cloud

1. Upload this folder to a GitHub repository.
2. Open Streamlit Community Cloud and create a new app.
3. Select the repository and branch.
4. Set the main file path to `streamlit_app.py`.
5. Deploy the app.

Open the deployed app and click **Open Branch Gap Radar Pro**. The dashboard is served from `/app/static/Branch_Gap_Radar_Pro.html`.

The dashboard asks for the Excel file in the browser. Stock data is processed in the browser and is not included in this repository or uploaded to Streamlit.
