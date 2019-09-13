"""This is an interpolation module."""

from datetime import datetime

from numpy import (sin, cos, tan, exp, linspace)  # pylint: disable=unused-import

from scipy.interpolate import interp1d

from bokeh.plotting import (figure, show, output_file)
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn


class Interpolation:
    """This is an interpolation class."""
    def __init__(self, start, stop, samples, function, first_kind,
                 second_kind):
        self.start = start
        self.stop = stop
        self.samples = samples
        self.function = function
        self.first_kind = first_kind
        self.second_kind = second_kind

        self.now = datetime.now().strftime("%d-%m-%Y")

        self.tooltips = []
        self.graph = None
        self.interp1d = None
        self.x_raw = 0.0
        self.y_raw = 0.0
        self.x_interp = 0.0
        self.y_interp = 0.0

        self.data = dict()
        self.source = None
        self.columns = []
        self.data_table = None
        self.kind = ""

    def interpolation_graph(self):
        """This is a function to draw an interpolation graph."""

        # Graph configuration
        self.tooltips = [("index", "$index"), ("(x, y)", "($x, $y)")]
        self.graph = figure(tooltips=self.tooltips)
        self.graph.title.text = self.function + " - " + self.first_kind + " - " + self.second_kind
        self.graph.xaxis.axis_label = "x"
        self.graph.yaxis.axis_label = self.function

        # Drawing the raw data graph
        self.x_raw = linspace(self.start, self.stop, num=self.samples)
        x = self.x_raw  #This is a temporary solution. Needed for eval function. pylint: disable=unused-variable, invalid-name
        self.y_raw = eval(self.function)  # pylint: disable=eval-used
        self.graph.circle(self.x_raw,
                          self.y_raw,
                          legend="raw data",
                          fill_color="#006600",
                          size=8)

        # Drawing the first kind of interpolation graph
        self.interp1d = interp1d(self.x_raw, self.y_raw, kind=self.first_kind)
        self.x_interp = linspace(self.start, self.stop, num=10 * self.samples)
        self.y_interp = self.interp1d(self.x_interp)
        self.graph.line(self.x_interp,
                        self.y_interp,
                        legend=self.first_kind,
                        line_color="#0033cc",
                        line_dash="solid")

        # Drawing the second kind of interpolation graph
        self.interp1d = interp1d(self.x_raw, self.y_raw, kind=self.second_kind)
        self.x_interp = linspace(self.start, self.stop, num=10 * self.samples)
        self.y_interp = self.interp1d(self.x_interp)
        self.graph.line(self.x_interp,
                        self.y_interp,
                        legend=self.second_kind,
                        line_color="#cc0000",
                        line_dash="dashed")

        # Legend configuration
        self.graph.legend.location = "bottom_left"
        self.graph.legend.click_policy = "hide"

        # Export graph to .html file
        output_file(self.now + ", " + self.first_kind + ", " +
                    self.second_kind + " - graph.html",
                    title=self.now + ", " + self.first_kind + ", " +
                    self.second_kind + " - graph.html")
        show(self.graph)

    def interpolation_table(self, kind):
        """This is a function to create a table with interpolation values."""

        self.kind = kind

        self.x_raw = linspace(self.start, self.stop, num=self.samples)
        x = self.x_raw  #This is a temporary solution. Needed for eval function. pylint: disable=unused-variable, invalid-name
        self.y_raw = eval(self.function)  # pylint: disable=eval-used

        self.interp1d = interp1d(self.x_raw, self.y_raw, kind=self.kind)
        self.x_interp = linspace(self.start, self.stop, num=10 * self.samples)
        self.y_interp = self.interp1d(self.x_interp)

        data = dict(x=self.x_interp, y=self.y_interp)
        self.source = ColumnDataSource(data)

        self.columns = [
            TableColumn(field="x",
                        title="x | " + self.function + " - " + self.kind),
            TableColumn(field="y", title="y")
        ]
        self.data_table = DataTable(source=self.source, columns=self.columns)

        output_file(self.now + ", " + self.kind + " - table.html",
                    title=self.now + ", " + self.kind + " - table.html")
        show(self.data_table)
