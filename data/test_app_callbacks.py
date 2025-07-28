import pytest
from dash.testing.application_runners import import_app

# Load the app from your module
@pytest.fixture
def app():
    app_instance = import_app("app")
    return app_instance

def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Sales Line Chart"

def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker is not None