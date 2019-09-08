"""This is an interpolation module."""

from numpy import (sin, cos, tan, exp, linspace)

from scipy.interpolate import interp1d

from bokeh.plotting import (figure, show, output_file)


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

        self.tooltips = []
        self.graph = None
        self.interp = None
        self.x_raw = 0.0
        self.y_raw = 0.0
        self.x_interp = 0.0
        self.y_interp = 0.0

    def interpolation_graph(self):
        """This is a function to draw an interpolation graph."""

        # Graph configuration
        self.tooltips = [("index", "$index"), ("(x, y)", "($x, $y)")]
        self.graph = figure(tooltips=self.tooltips)
        self.graph.title.text = self.function + " - graph"
        self.graph.xaxis.axis_label = "x"
        self.graph.yaxis.axis_label = self.function

        # Drawing the raw data graph
        self.x_raw = linspace(self.start, self.stop, num=self.samples)
        x = self.x_raw  #This is a temporary solution. Needed for eval function.
        self.y_raw = eval(self.function)
        self.graph.circle(self.x_raw,
                          self.y_raw,
                          legend="raw data",
                          fill_color="#006600",
                          size=8)

        # Drawing the first kind of interpolation
        self.interp = interp1d(self.x_raw, self.y_raw, kind=self.first_kind)
        self.x_interp = linspace(self.start, self.stop, num=10 * self.samples)
        self.y_interp = self.interp(self.x_interp)
        self.graph.line(self.x_interp,
                        self.y_interp,
                        legend=self.first_kind,
                        line_color="#0033cc",
                        line_dash="solid")

        # Drawing the second kind of interpolation
        self.interp = interp1d(self.x_raw, self.y_raw, kind=self.second_kind)
        self.x_interp = linspace(self.start, self.stop, num=10 * self.samples)
        self.y_interp = self.interp(self.x_interp)
        self.graph.line(self.x_interp,
                        self.y_interp,
                        legend=self.second_kind,
                        line_color="#cc0000",
                        line_dash="dashed")

        # Legend configuration
        self.graph.legend.location = "bottom_left"
        self.graph.legend.click_policy = "hide"

        # Generating a .html file
        output_file("InterpolationComparison_results.html",
                    title=self.function + " - graph")
        show(self.graph)
