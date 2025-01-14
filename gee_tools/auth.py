import ee
import google.auth.compute_engine

def initialize_gee(project_id, opt_url='https://earthengine-highvolume.googleapis.com'):
    """
    Initialize Earth Engine with authentication
    
    Parameters:
    project_id (str): GEE project ID (e.g., 'ee-ehsanjalilvand')
    opt_url (str): Optional URL for high-volume endpoint
    """
    try:
        credentials = google.auth.compute_engine.Credentials()
        ee.Authenticate(force=True)
        ee.Initialize(project=project_id, opt_url=opt_url)
        print("Successfully authenticated and initialized Earth Engine")
    except Exception as e:
        raise Exception(f"Failed to initialize Earth Engine: {str(e)}")