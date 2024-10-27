def print_versions():
    try:
        import pandas

        print(f"Pandas version: {pandas.__version__}")
    except ImportError:
        print("Pandas is not installed.")

    try:
        import requests

        print(f"Requests version: {requests.__version__}")
    except ImportError:
        print("Requests is not installed.")
