# GitHub Actions Workflow for Parallel Processing Notebook

This workflow automatically executes the `Parallel Processing.ipynb` notebook and publishes the results.

## Features

- ✅ Automatically executes all cells in the notebook
- ✅ Converts results to HTML for easy viewing
- ✅ Creates a summary of outputs in Markdown
- ✅ Publishes results as GitHub Releases
- ✅ Archives artifacts for 90 days

## Triggers

The workflow runs in the following scenarios:

1. **Manual Trigger**: Use the "Run workflow" button in GitHub Actions tab
2. **On Push**: When changes are made to `Parallel Processing.ipynb` or the workflow file
3. **Scheduled**: Weekly on Sundays at midnight UTC

## How to Use

### Manual Execution

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. Select "Run Parallel Processing Notebook" from the workflows list
4. Click "Run workflow" button
5. Select the branch and click "Run workflow"

### View Results

After the workflow completes:

1. **Releases**: Go to the "Releases" section to download:
   - HTML report (`Parallel_Processing_Results.html`)
   - Executed notebook (`Parallel Processing.ipynb`)
   - Complete results archive (`.zip`)

2. **Artifacts**: In the Actions tab, click on a workflow run to download artifacts (available for 90 days)

3. **Summary**: The release notes contain a summary of execution outputs

## Outputs

Each run produces:

- **HTML Report**: Fully rendered notebook with all outputs and visualizations
- **Executed Notebook**: Updated `.ipynb` file with all cell outputs
- **Results Summary**: Markdown file with execution statistics and text outputs
- **ZIP Archive**: Complete package of all results

## Configuration

### Timeout

The notebook execution timeout is set to 3600 seconds (1 hour). To adjust:

```yaml
--ExecutePreprocessor.timeout=3600
```

### Schedule

To change the schedule, modify the cron expression:

```yaml
schedule:
  - cron: '0 0 * * 0'  # Weekly on Sunday at midnight UTC
```

### Python Version

Current version: Python 3.11. To change:

```yaml
python-version: '3.11'
```

## Dependencies

The workflow installs:
- jupyter
- nbconvert
- pandas
- numpy
- requests
- matplotlib
- seaborn
- mlxtend
- scipy
- scikit-learn

## Notes

- The workflow downloads `Trips_2018.csv` during execution (not included in releases due to size)
- Artifacts are retained for 90 days
- Releases are created only for manual and scheduled runs (not for push events)

## Troubleshooting

If the workflow fails:

1. Check the Actions tab for error logs
2. Verify all dependencies are correctly installed
3. Ensure the notebook doesn't have cells that require user input
4. Check if the CSV download URL is accessible

## Permissions

The workflow requires the following permissions (already configured):
- `contents: write` - To create releases
- `actions: read` - To access workflow artifacts
