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

Open the deployed app and click **Open Branch Gap Radar Pro**. On Streamlit Community Cloud, the dashboard is served from `/~/+/app/static/Branch_Gap_Radar_Pro.html`.

The dashboard first asks for the stock Excel file. Sales and purchase registers
can then be added for purchasing intelligence. All files are processed in the
browser; they are not included in this repository or uploaded to Streamlit.

The current dashboard supports colour, series and size gap matrices, branch
ranking, exact duplicates, product and brand share analysis, optional ideal-map
slot compliance, and Excel report export. SheetJS and ExcelJS are embedded in
the HTML so the data and report logic do not depend on a third-party CDN.

With sales data loaded, the dashboard also provides demand-based stock movement
suggestions, 40/60-day slow-stock analysis, branch stock requirements,
quantity-only category POs, item sale history and category/product-wise salesman
ranking. Purchase data adds receipt timing to the critical slow-stock rules.
