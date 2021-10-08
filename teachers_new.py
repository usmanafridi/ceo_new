import dash
from dash import html
import dash_table
from dash import dcc
import dash_bootstrap_components as dbc
from dash import Input,Output
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('E:/table.csv')

year=['2018', '2019', '2020', '2021']

semester=['Spring', 'Fall']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout= html.Div([

html.Div([

html.Div([

				html.Div([
					html.Label(['Select Year/عام']),
					dcc.Dropdown(
						id="dropdown(teacher)",
						options=[{"label": 2021, "value": 2021} for x in year],
						value=year[0],
						clearable=False,
					),
				]),

		html.Div([
					html.Label(['Select Semester/حدد الفصل الدراسي']),
					dcc.Dropdown(
						id="dropdown1(teacher)",
						options=[{"label": x, "value": x} for x in semester],
						value=semester[0],
						clearable=False,

					),
				]),
],className='new')
		],className = "row"),


	html.Div([

			html.Div([
				dcc.Graph(id='bar_chart3',config={"displayModeBar": "hover"})
			],className='experience'),


			html.Div([

dash_table.DataTable(

    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)
			],className='table1')

	],className='row'),





html.Div([

	html.Div([

		dcc.Graph(
			id='bar_chart',
			config={"displayModeBar": "hover"}
		)

	],className='container_new'),


	html.Div([

		dcc.Graph(id='bar_chart2', config={"displayModeBar": "hover"})
	],className='container_other '),

],className="row")


],className='main_layout')



@app.callback(
    Output(component_id='bar_chart', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year,semester):

    values = ['Pakistan',
'India',
'Canada',
'South Africa',
'United Kingdom',
'Nepal'
]
    labels = [29,
41,
30,
15,
20,
25,
]

    fig = {
		"data": [
			go.Bar(
				x=labels,
				y=values,
				name="Teachers Nationality",
				marker={
					"color": "rgb(219, 191, 249)"
				},
				orientation='h'

			),

		],

		"layout": go.Layout(
			title={
				"text": f" جنسية المعلم/Teacher Nationality  ",
				"y": 0.93,
				"x": 0.5,
				"xanchor": "center",
				"yanchor": "top"
			},
			titlefont={
				"color": "black",
				"size": 15
			},
			xaxis={
				"title": "<b>Nationality/جنسية</b>",
				"color": "black",
				"showline": True,
				"showgrid": False,
				"showticklabels": True,

				"linecolor": "black",
				"linewidth": 1,
				"ticks": "outside",
				"tickfont": {
					"family": "Aerial",
					"color": "black",
					"size": 12
				}
			},
			yaxis={
				"title": "<b>Number of teachers/عدد المعلمين</b>",
				"color": "black",
				"showline": True,
				"showgrid": False,
				"showticklabels": True,
				"linecolor": "white",
				"linewidth": 1,
				"ticks": "outside",
				"tickfont": {
					"family": "Aerial",
					"color": "black",
					"size": 12
				}
			},
			font={
				"family": "sans-serif",
				"color": "black",
				"size": 12
			},
			hovermode="closest",
			paper_bgcolor="white",
			plot_bgcolor="white",
			legend={
				"orientation": "h",
				"bgcolor": "black",
				"xanchor": "center",
				"x": 0.5,
				"y": -0.7
			}
		)

	}
    return fig



@app.callback(
    Output(component_id='bar_chart2', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year, term):


    fig = {
        "data": [
            go.Bar(
                x=['30','40', '50', '60' ],
                y=[100, 90, 80, 70],
                name="Department Wise",
                marker={
                    "color": "#DD4B39",
				},
                hoverinfo="text",

            ),


        ],


        "layout": go.Layout(
            title={
                "text": f" Teachers age group/فئة المعلمين العمرية  ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 15
            },
            xaxis={
                "title": "<b>Age group/الفئة العمرية</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                'categoryorder': 'total descending',
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "Number of teachers/عدد المعلمين",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "black",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="white",
            plot_bgcolor="white",
            legend={
                "orientation": "h",
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig


@app.callback(
    Output(component_id='bar_chart3', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year,semester):

    values = ['Pakistan',
'India',
'Canada',
'South Africa',
'United Kingdom',
'Nepal'
]
    labels = [29,
41,
30,
15,
20,
25,
]

    fig = {
		"data": [
			go.Bar(
				x=labels,
				y=values,
				name="Teachers Nationality",
				marker={
					"color": "rgb(219, 191, 249)"
				},
				orientation='h'

			),

		],

		"layout": go.Layout(
			title={
				"text": f" جنسية المعلم/Teacher Nationality  ",
				"y": 0.93,
				"x": 0.5,
				"xanchor": "center",
				"yanchor": "top"
			},
			titlefont={
				"color": "black",
				"size": 15
			},
			xaxis={
				"title": "<b>Nationality/جنسية</b>",
				"color": "black",
				"showline": True,
				"showgrid": False,
				"showticklabels": True,

				"linecolor": "black",
				"linewidth": 1,
				"ticks": "outside",
				"tickfont": {
					"family": "Aerial",
					"color": "black",
					"size": 12
				}
			},
			yaxis={
				"title": "<b>Number of teachers/عدد المعلمين</b>",
				"color": "black",
				"showline": True,
				"showgrid": False,
				"showticklabels": True,
				"linecolor": "white",
				"linewidth": 1,
				"ticks": "outside",
				"tickfont": {
					"family": "Aerial",
					"color": "black",
					"size": 12
				}
			},
			font={
				"family": "sans-serif",
				"color": "black",
				"size": 12
			},
			hovermode="closest",
			paper_bgcolor="white",
			plot_bgcolor="white",
			legend={
				"orientation": "h",
				"bgcolor": "black",
				"xanchor": "center",
				"x": 0.5,
				"y": -0.7
			}
		)

	}
    return fig



if __name__=='__main__':
    app.run_server(debug=True)