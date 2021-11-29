import sqlalchemy

class Database:
    # Create SQL database connection object
    def __init__(self):
        self.host = "sg1-ss19.a2hosting.com"
        self.port = "5432"
        self.db = "madsahos_capstone2021fall"
        self.name = "madsahos_capstone2021co2"
        self.pw = "FQU2kSfSoCo9mFJmGstvEa5HD1gSqPhh3b3vqU0yOoRk2L61wjKQcuqyB5Vs"
        self.config = f"postgresql://{self.name}:{self.pw}@{self.host}:{self.port}/{self.db}"
        self.engine = sqlalchemy.create_engine(self.config)
        self.connection = self.engine.connect()
        self.metadata = sqlalchemy.MetaData()

# Must always have these two features
class Core:
    def __init__(self):
        _essential = ['iso_code', 'year']

        # These are the complete list of features from the dataset
        _base = [
            'co2', 'consumption_co2', 'trade_co2', 'coal_co2', 'cement_co2',
            'flaring_co2', 'gas_co2', 'oil_co2', 'other_industry_co2',
            'methane', 'nitrous_oxide', 'population', 'gdp', 'primary_energy_consumption']

        _derived = [
            'co2_growth_prct', 'co2_growth_abs', 'co2_per_capita', 'consumption_co2_per_capita',
            'share_global_co2', 'cumulative_co2', 'share_global_cumulative_co2', 'co2_per_gdp',
            'consumption_co2_per_gdp', 'co2_per_unit_energy', 'cement_co2_per_capita',
            'coal_co2_per_capita', 'flaring_co2_per_capita', 'gas_co2_per_capita',
            'oil_co2_per_capita', 'other_co2_per_capita', 'trade_co2_share',
            'share_global_cement_co2', 'share_global_coal_co2', 'share_global_flaring_co2',
            'share_global_gas_co2', 'share_global_oil_co2', 'share_global_other_co2',
            'cumulative_cement_co2', 'cumulative_coal_co2', 'cumulative_flaring_co2',
            'cumulative_gas_co2', 'cumulative_oil_co2', 'cumulative_other_co2',
            'share_global_cumulative_cement_co2', 'share_global_cumulative_coal_co2',
            'share_global_cumulative_flaring_co2', 'share_global_cumulative_gas_co2',
            'share_global_cumulative_oil_co2', 'share_global_cumulative_other_co2', 'total_ghg',
            'ghg_per_capita', 'methane_per_capita', 'nitrous_oxide_per_capita',
            'energy_per_capita', 'energy_per_gdp']

        _new = [
            'urban_population_percent', 'constant_gdp_per_capita', 'energy_intensity', 'manufacturing__pct', 'trade_openness', 
            'renewable_energy_consumption_share', 'percent_of_environment_patent']

        self.all_features = []
        self.derived_features = []
        self.base_features = []
        self.new_features = []

        self.base_features.extend(_essential)
        self.base_features.extend(_base)

        self.derived_features.extend(_essential)
        self.derived_features.extend(_derived)

        self.new_features.extend(_essential)
        self.new_features.extend(_new)
        

        self.all_features.extend(_essential)
        self.all_features.extend(_base)
        self.all_features.extend(_derived)
        self.all_features.extend(_new)

        self.world = "all"
        self.regions = {'global': [self.world],
                        'usa': ['USA'],
                        'china': ['CHN']
                        }
        self.list_of_regions = [*self.regions]
        self.excluded_features = ['OWID_WRL']
        #
        # self.regression_features = self.base_features
        _selected =[]
        _selected.extend(_essential)
        _selected.extend(['consumption_co2'])
        self.regression_features = self.all_features
        self.clustering_features = self.base_features