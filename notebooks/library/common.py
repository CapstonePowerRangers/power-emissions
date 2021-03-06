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

        self.regression_cv = 5
        self.error_optimise = 'MSE'
        self.regression_normalize = True
        self.normalize_method = 'minmax'
        self.remove_outliers = False
        self.outliers_threshold = 0.05
        self.silent_mode = True
        self.start_year = 1971
        self.stop_year = 2016

        processed_path = Path.cwd().parent/'data'
        processed_path = processed_path/'processed'
        processed_path = processed_path/'master_dataset.pkl'
        full_path = processed_path.as_posix()
        _dataset = pd.read_pickle(full_path)
        _dataset = _dataset[_dataset.iso_code != 'WLD']

        self.dataset = _dataset


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

        _relevant = ['co2', 'consumption_co2', 'co2_growth_prct',
                     'co2_growth_abs', 'trade_co2', 'co2_per_capita', 'consumption_co2_per_capita',
                     'share_global_co2', 'cumulative_co2', 'share_global_cumulative_co2', 'co2_per_gdp',
                     'consumption_co2_per_gdp', 'co2_per_unit_energy',
                     'coal_co2', 'coal_co2_per_capita',  'share_global_coal_co2', 'cumulative_coal_co2',  'share_global_cumulative_coal_co2',
                     'gas_co2', 'oil_co2', 'gas_co2_per_capita', 'share_global_gas_co2', 'cumulative_gas_co2', 'share_global_cumulative_gas_co2',
                     'oil_co2_per_capita', 'cumulative_oil_co2', 'share_global_cumulative_oil_co2',
                     'other_co2_per_capita', 'trade_co2_share',
                     'share_global_oil_co2', 'cumulative_other_co2',
                     'share_global_other_co2', 'share_global_cumulative_other_co2',
                     'population',
                     'gdp',
                     'primary_energy_consumption', 'energy_per_capita', 'energy_per_gdp',
                     'current_gdp', 'constant_gdp', 'manufacturing_gdp',
                     'medium_to_high_tech_percent', 'export', 'import', 'real_gdp_growth_percent',
                     'urban_population_percent', 'merchandise_export', 'merchandise_import',
                     'manufacturer_export_share', 'manufacturer_export', 'co2_emission_electricity',
                     'co2_emission_other_fuel',
                     'co2_emission_transport',
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

        self.relevant_features = []
        self.relevant_features.extend(_essential)
        self.relevant_features.extend(_relevant)

        self.categorical = []
        self.categorical.extend(_essential)
        self.categorical.extend((_categorical))

        self.world = "WLD"

        # Reads in the clustering information and returns iso codes for
        # each country in the cluster.
        from pathlib import Path
        import json

        try:
            _cluster_path = (Path.cwd().parent / 'data/processed/final_cluster_3.json').as_posix()
            with open(_cluster_path, 'r') as _cluster_data:
                _clustering = json.load(_cluster_data)
            _c_df = pd.DataFrame.from_dict(_clustering, orient = 'columns')
            _c_df = _c_df[['iso_code', 'Cluster']]
            self.regions = _c_df.groupby('Cluster')['iso_code'].apply(list).to_dict()
            self.regions['Global'] = [self.world]
            self.list_of_regions = [*self.regions]
            self.excluded_features = ['OWID_WRL']

        except:
            pass

        # # override (temp) clusters
        # self.list_of_regions = [self.world]

        self.co2_features = [
            'year', 'iso_code', 'co2'
        ]

        self.regression_features = [
        'year', 'iso_code',
        'population',
        'constant_gdp_per_capita',
        'energy_intensity',
        'manufacturing_percent',
        'trade_openness',
        'renewable_energy_consumption_share'


            # 'year', 'iso_code', 'region', 'income_group',
            # 'co2', 'co2_emission_per_capita', 'co2_emission_per_constant_gdp',
            # 'population', 'urban_population_percent', 'constant_gdp_per_capita',
            # 'manufacturing_percent', 'manufacturing_country_share_percent', 'trade_openness',
            # 'primary_energy_consumption_per_capita', 'renewable_energy_consumption_share',
            # 'percent_of_environment_patent', 'energy_intensity'
        ]

        self.clustering_features = [
            'year', 'iso_code', 'co2', 'consumption_co2', 'trade_co2',
            'co2_per_unit_energy', 'coal_co2',
            'gas_co2', 'oil_co2',
            # 'other_industry_co2',
            'population', 'gdp', 'primary_energy_consumption',
            'current_gdp', 'constant_gdp', 'manufacturing_gdp',
            'medium_to_high_tech_percent', 'export', 'import',
            'urban_population_percent', 'merchandise_export', 'merchandise_import',
            'manufacturer_export', 'co2_emission_electricity',
            # 'co2_emission_manufacturing',
            'co2_emission_other_fuel',
            # 'co2_emission_fugitive',
            'co2_emission_transport',
            'co2_emission_industrial_process',
            'medium_to_high_tech_gdp',  'industrial_gdp',  'iea_primary_energy_consumption',
            'renewable_energy_consumption', 'coal_consumption', 'oil_consumption',
            'total_electricity_production', 'electricity_production_from_renewable',
            'energy_intensity', 'percent_of_environment_patent'
        ]
    def get_cluster_data(self, year):
        df = self.dataset.copy()
        df = df[df.year == year]
        df = df[self.clustering_features].fillna(0)
        return df

    def features(self):
        return list(self.dataset.columns)

    def feature_data(self, feature = '', first = 0, last = 9999):
        f_list = []
        if len(feature) > 0:
            f_list =['year', 'iso_code']
            if isinstance(feature, list):
                print(type(feature))
                f_list.extend(feature)
            else:
                f_list.append(feature)
        result = (self.dataset[f_list] if len(feature)>1 else self.dataset)

        result = result[result.year.ge(first)]
        result = result[result.year.le(last)]
        return result


    def get_cluster_regression_datas(self,
                                     cluster = 'Global',
                                     first = 0,
                                     last = 9999):

        _df = self.dataset.copy()
        _selected = self.regression_features.copy()

        _selected.append('co2')

        if not(cluster == 'Global'):
            _df = _df[_df.iso_code.isin(self.regions.get(cluster))]

        _df = _df[_selected]
        _df = _df[_df.year.ge(first)]
        _df = _df[_df.year.le(last)]
        _df = _df.drop (columns = 'iso_code')
        _df = _df.groupby('year').sum()

        return _df.reset_index(drop = True)

    def check_start_override(self, feature, _default):

        _override = {'co2_per_unit_energy': 1980,
                     'co2_per_capita': 1950,
                     'co2_per_gdp': 1950,
                     'co2_emission_per_constant_gdp': 1980,
                     'other_co2_per_capita': 1990,
                     'oil_co2_per_capita': 1950,

                     'population': 1950,

                     'primary_energy_consumption': 1980,
                     'coal_consumption': 1971,
                     'fossil_energy_consumption_share': 1971,
                     'renewable_energy_consumption': 1990,
                     'renewable_energy_consumption_share': 1990,
                     'renewable_electricity_production_share': 1990,

                     'percent_of_environment_patent': 1985,

                     'manufacturer_export_share': 1989,

                     'energy_per_capita': 1980,
                     'energy_per_gdp': 1980,
                     'constant_gdp_per_capita': 1970,
                     'iea_primary_energy_consumption': 1971,
                     'primary_energy_consumption_per_capita': 1971,
                     'energy_intensity': 1990,
                     }
        _result = _override.get(feature)
        return (_default if _result == None else _result)

    def get_forecasts(self):
        import pickle
        import pandas as pd
        from pathlib import Path
        cwd = Path.cwd()
        fc_path = cwd.parent / r'data/processed/ts_forecast.pkl'

        with open(fc_path, 'rb') as fc_file:
            _df = pd.DataFrame(pickle.load(fc_file), columns = ['cluster', 'feature', 'forecast'])

        _r = []
        _c_list = list(_df.cluster.unique())
        _f_list = list(_df.feature.unique())

        for _c in _c_list:
            _cdf = pd.DataFrame()
            for _f in _f_list:
                _fc = _df.loc[_df.feature.eq(_f) & _df.cluster.eq(_c), 'forecast'].copy().to_numpy()
                _fc = pd.DataFrame(_fc[0], columns = ['year', _f])
                if len(_cdf) == 0:
                    _cdf = _fc
                else:
                    _f_fc = _fc.loc[:, _f]
                    _cdf = _cdf.join(_f_fc)
                _cdf['cluster'] = _c
            if len(_r) == 0:
                _r = _cdf.copy()
            else:
                _r = _r.append(_cdf)
        _r.year = _r.year.astype('int')
        return _r



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