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
        from pathlib import Path
        import pandas as pd

        processed_path = Path.cwd().parent/'data'
        processed_path = processed_path/'processed'
        processed_path = processed_path/'master_dataset.pkl'
        full_path = processed_path.as_posix()
        self.dataset = pd.read_pickle(full_path)

        _all = ['country', 'co2', 'consumption_co2', 'co2_growth_prct',
                'co2_growth_abs', 'trade_co2', 'co2_per_capita', 'consumption_co2_per_capita',
                'share_global_co2', 'cumulative_co2', 'share_global_cumulative_co2', 'co2_per_gdp',
                'consumption_co2_per_gdp', 'co2_per_unit_energy', 'coal_co2', 'cement_co2',
                'flaring_co2', 'gas_co2', 'oil_co2', 'other_industry_co2', 'cement_co2_per_capita',
                'coal_co2_per_capita', 'flaring_co2_per_capita', 'gas_co2_per_capita',
                'oil_co2_per_capita', 'other_co2_per_capita', 'trade_co2_share', 'share_global_cement_co2',
                'share_global_coal_co2', 'share_global_flaring_co2', 'share_global_gas_co2',
                'share_global_oil_co2', 'share_global_other_co2', 'cumulative_cement_co2',
                'cumulative_coal_co2', 'cumulative_flaring_co2', 'cumulative_gas_co2',
                'cumulative_oil_co2', 'cumulative_other_co2', 'share_global_cumulative_cement_co2',
                'share_global_cumulative_coal_co2', 'share_global_cumulative_flaring_co2',
                'share_global_cumulative_gas_co2', 'share_global_cumulative_oil_co2',
                'share_global_cumulative_other_co2', 'total_ghg', 'ghg_per_capita', 'methane',
                'methane_per_capita', 'nitrous_oxide', 'nitrous_oxide_per_capita', 'population',
                'gdp', 'primary_energy_consumption', 'energy_per_capita', 'energy_per_gdp',
                'current_gdp', 'constant_gdp', 'manufacturing_gdp',
                'medium_to_high_tech_percent', 'export', 'import', 'real_gdp_growth_percent',
                'urban_population_percent', 'merchandise_export', 'merchandise_import',
                'manufacturer_export_share', 'manufacturer_export', 'co2_emission_electricity',
                'co2_emission_building', 'co2_emission_manufacturing', 'co2_emission_other_fuel',
                'co2_emission_fugitive', 'co2_emission_transport', 'co2_emission_energy_subtotal',
                'co2_emission_bunkers', 'co2_emission_industrial_process', 'co2_emission_per_capita',
                'constant_gdp_per_capita', 'manufacturing_percent', 'medium_to_high_tech_gdp',
                'co2_emission_per_constant_gdp', 'trade_openness', 'share_of_merchandise_export',
                'share_of_merchandise_import', 'industrial_gdp', 'co2_country_share_percent',
                'manufacturing_country_share_percent', 'iea_primary_energy_consumption',
                'renewable_energy_consumption', 'coal_consumption', 'oil_consumption',
                'total_electricity_production', 'electricity_production_from_renewable',
                'primary_energy_consumption_per_capita', 'fossil_energy_consumption_share',
                'renewable_electricity_production_share', 'energy_intensity',
                'renewable_energy_consumption_share', 'percent_of_environment_patent']

        _categorical = [
            'region', 'income_group']

        _excluded = ['co2_emission_energy_subtotal',]
        _essential = ['iso_code', 'year']

        # These are the complete list of features from the dataset
        _base = [
            'co2', 'consumption_co2', 'trade_co2',
            'co2_per_unit_energy', 'coal_co2', 'cement_co2',
            'flaring_co2', 'gas_co2', 'oil_co2', 'other_industry_co2', 'total_ghg', 'methane',
            'nitrous_oxide', 'population', 'gdp', 'primary_energy_consumption',
            'current_gdp', 'constant_gdp', 'manufacturing_gdp',
            'medium_to_high_tech_percent', 'export', 'import',
            'urban_population_percent', 'merchandise_export', 'merchandise_import',
            'manufacturer_export', 'co2_emission_electricity',
            'co2_emission_building', 'co2_emission_manufacturing', 'co2_emission_other_fuel',
            'co2_emission_fugitive', 'co2_emission_transport',
            'co2_emission_bunkers', 'co2_emission_industrial_process',
            'medium_to_high_tech_gdp',  'industrial_gdp',  'iea_primary_energy_consumption',
            'renewable_energy_consumption', 'coal_consumption', 'oil_consumption',
            'total_electricity_production', 'electricity_production_from_renewable',
            'energy_intensity', 'percent_of_environment_patent'
        ]

        _derived = [
            'manufacturing_percent', 'manufacturer_export_share', 'trade_openness', 'share_of_merchandise_export',
            'share_of_merchandise_import','primary_energy_consumption_per_capita', 'fossil_energy_consumption_share',
            'renewable_electricity_production_share', 'renewable_energy_consumption_share',
            'co2_growth_prct', 'co2_growth_abs', 'co2_per_capita', 'consumption_co2_per_capita',
            'share_global_co2', 'cumulative_co2', 'share_global_cumulative_co2', 'co2_per_gdp',
            'consumption_co2_per_gdp', 'cement_co2_per_capita',
            'coal_co2_per_capita', 'flaring_co2_per_capita', 'gas_co2_per_capita',
            'oil_co2_per_capita', 'other_co2_per_capita', 'trade_co2_share', 'share_global_cement_co2',
            'share_global_coal_co2', 'share_global_flaring_co2', 'share_global_gas_co2',
            'share_global_oil_co2', 'share_global_other_co2', 'cumulative_cement_co2',
            'cumulative_coal_co2', 'cumulative_flaring_co2', 'cumulative_gas_co2',
            'cumulative_oil_co2', 'cumulative_other_co2', 'share_global_cumulative_cement_co2',
            'share_global_cumulative_coal_co2', 'share_global_cumulative_flaring_co2',
            'share_global_cumulative_gas_co2', 'share_global_cumulative_oil_co2',
            'share_global_cumulative_other_co2', 'ghg_per_capita',  'methane_per_capita',
            'nitrous_oxide_per_capita', 'energy_per_capita', 'energy_per_gdp','real_gdp_growth_percent',
            'co2_emission_per_capita', 'constant_gdp_per_capita', 'co2_emission_per_constant_gdp',
            'co2_country_share_percent', 'manufacturing_country_share_percent'
        ]

        self.base_features = []
        self.base_features.extend(_essential)
        self.base_features.extend(_base)

        self.derived_features = []
        self.derived_features.extend(_essential)
        self.derived_features.extend(_derived)

        self.all_features = []
        self.all_features.extend(_essential)
        self.all_features.extend(_base)
        self.all_features.extend(_derived)

        self.categorical = []
        self.categorical.extend(_essential)
        self.categorical.extend((_categorical))

        self.world = "WLD"
        self.regions = {'global': [self.world],
                        'usa': ['USA'],
                        'china': ['CHN']
                        }
        self.list_of_regions = [*self.regions]
        self.excluded_features = ['OWID_WRL']

        self.regression_features = [
            'year', 'iso_code', 'region', 'income_group',
            'co2', 'co2_emission_per_capita', 'co2_emission_per_constant_gdp',
            'population', 'urban_population_percent', 'constant_gdp_per_capita',
            'manufacturing_percent', 'manufacturing_country_share_percent', 'trade_openness',
            'primary_energy_consumption_per_capita', 'renewable_energy_consumption_share',
            'percent_of_environment_patent', 'energy_intensity'
        ]

        self.clustering_features = self.base_features

    def get_cluster_data(self, year):
        df = self.dataset.copy()
        df = df[df.year == year]
        df = df[self.clustering_features].fillna(0)
        return df

    def features(self):
        return list(self.dataset.columns)

    def feature_data(self, feature = '', first = 0, last = 9999):
        if len(feature) > 0:
            f_list =['year', 'iso_code']
            f_list.append(feature)
        result = (self.dataset[f_list] if len(feature)>1 else self.dataset)

        result = result[result.year.ge(first)]
        result = result[result.year.le(last)]

        return result


def clean_column_names(df):

    cleaned_names = []
    list_of_cols = list(df.columns)

    for c in list_of_cols:
        c = c.strip()
        c = c.lower()
        c = c.replace(".", "_")
        c = c.replace(" ", "_")
        c = c.replace("%", "_pct")
        cleaned_names.append(c)

    return cleaned_names