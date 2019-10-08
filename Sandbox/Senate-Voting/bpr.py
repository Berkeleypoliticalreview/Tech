"""

Berkeley Political Review
Data Visualization

Custom Assets


Created By: James Weichert 10/5/19

"""

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
import chart_studio.plotly as pl
import plotly.express as px
import plotly.graph_objects as go


#===Partisan Data Color Scales===

dem_rep = ["#487EBF",  "#BF424A"]
safe_tossup = ["#444CA0", "#F2DDA9", "#A04555"]
safe_leans_tossup = ["#444CA0", "#81B6E8", "#F2DDA9", "#DD758A", "#A04555"]
safe_likely_leans_tossup = ["#444CA0", "#487EBF", "#81B6E8", "#F2DDA9", "#DD758A", "#BF424A", "#A04555"]



#===Chart-Generating Functions===

def create_us_state_map(data, z_col, state_col='State', map_title="[MAP TITLE]", cb_title="[UNIT LABEL]", c="Purples"):
    fig = go.Figure(
        data = go.Choropleth (
            locations = data[state_col],
            z = data[z_col].astype(float),
            locationmode = 'USA-states',
            colorscale = c,
            colorbar_title = cb_title 
        )
    )
    
    fig.update_layout (
        title_text = map_title,
        geo_scope = 'usa',
        dragmode = False
    )
    
    fig.show()
    
    return fig