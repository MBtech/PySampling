from lhs import LHS
samples = LHS("sample.yaml", criteria='maximin')
samples.createSamples(10)
configs = samples.getSamplesAsList()
print configs
