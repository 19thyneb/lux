from lux.vizLib.altair.AltairChart import AltairChart
import altair as alt
alt.data_transformers.disable_max_rows()
class Histogram(AltairChart):
	def __init__(self,view):
		super().__init__(view)
	def __repr__(self):
		return f"Histogram <{str(self.view)}>"
	def initializeChart(self):
		self.tooltip = False
		xAttr = self.view.getObjFromChannel("x")[0].attribute

		chart = alt.Chart(self.data).mark_bar(size=12).encode(
			alt.X(xAttr, type="quantitative"),#, bin=alt.Bin(maxbins=50)),
			alt.Y("Count of Records (binned)", type="quantitative")
		)
		return chart 