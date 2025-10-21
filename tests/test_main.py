from pathlib import Path

test_dir=Path(__file__).resolve().parent
project_dir=test_dir.parent
print(project_dir)

data_dir=project_dir/"data"
raw_data_dir=data_dir/"raw"
log_dir=project_dir/"logs"
log_file=log_dir/"app.log"
def test_directories_exist():
    assert data_dir.exists(), f"Data directory {data_dir} does not exist."
    assert raw_data_dir.exists(), f"Raw data directory {raw_data_dir} does not exist."
    assert log_dir.exists(), f"Log directory {log_dir} does not exist."

