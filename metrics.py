from opencensus.ext.azure.metrics_exporter import new_metrics_exporter
from opencensus.stats import stats as stats_module
from opencensus.stats import measure as measure_moduleeeee
from opencensus.stats import view as view_module
from opencensus.stats import aggregation as aggregation_module
from opencensus.tags import tag_map as tag_map_module

exporter = new_metrics_exporter(connection_string="InstrumentationKey=a55d6c05-206b-438c-94d1-51176abb1f19;IngestionEndpoint=https://eastus2-3.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus2.livediagnostics.monitor.azure.com/;ApplicationId=1e557ba3-a5ec-4971-8b2a-ba849d53c5dc")
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
