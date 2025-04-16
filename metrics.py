from opencensus.ext.azure.metrics_exporter import new_metrics_exporter
from opencensus.stats import stats as stats_module
from opencensus.stats import measure as measure_module
from opencensus.stats import view as view_module
from opencensus.stats import aggregation as aggregation_module
from opencensus.tags import tag_map as tag_map_module

exporter = new_metrics_exporter(connection_string="InstrumentationKey=<INSTRUMENTATION_KEY>")
stats_module.stats.view_manager.register_exporter(exporter)

m_latency = measure_module.MeasureFloat("ocr_latency", "Latência do OCR", "ms")
view = view_module.View("ocr_latency_distribution", "Distribuição de latência do OCR", [],
                        m_latency, aggregation_module.DistributionAggregation([100, 500, 1000, 2000, 5000]))
stats_module.stats.view_manager.register_view(view)

def track_ocr_time(value_ms: float):
    mmap = stats_module.stats.stats_recorder.new_measurement_map()
    tmap = tag_map_module.TagMap()
    mmap.measure_float_put(m_latency, value_ms)
    mmap.record(tmap)
