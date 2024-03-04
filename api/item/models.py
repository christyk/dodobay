from django.db import models

# Item categories matching tab names of Data Spreadsheet for Animal Crossing New Horizons
# https://docs.google.com/spreadsheets/d/13d_LAJPlxMa_DubPTuirkIV4DERBMXbrWQsmSh8ReK4/edit#gid=371893803

class Category(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, primary_key=True)
    table_name = models.CharField(db_column='TABLE_NAME', max_length=255, blank=True, null=True)
    class_name = models.CharField(db_column='CLASS_NAME', max_length=255, blank=True, null=True)
    tradable = models.BooleanField(db_column='TRADABLE', blank=True, null=True)

    class Meta:
        db_table = 'CATEGORIES'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name + ' (' + self.class_name + ')'
    
# Item Index table combining identification and search fields of all items from all categories
    
class Item(models.Model):
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255, null=False)
    image = models.CharField(db_column='IMAGE', max_length=255, null=False, default='NA')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)#, limit_choices_to={'tradable': True})
    variation = models.CharField(db_column="VARIATION", max_length=255, null=False, default='NA')
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, null=False, default='NA')
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, null=False, default='NA')
    source = models.CharField(db_column="SOURCE", max_length=255, null=False, default='NA')
    season_event = models.CharField(db_column="SEASON_EVENT", max_length=255, null=False, default='NA')
    buy = models.CharField(db_column="BUY", max_length=20, null=False, default='NA')
    sell = models.CharField(db_column="SELL", max_length=20, null=False, default='NA')
    
    class Meta:
        db_table = 'ITEMS'

    def __str__(self):
        return self.name + ' (' + self.category.name + ' ' + self.color_1 + ' ' + self.color_2 + ')'


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# Tables for items extracted from Data Spreadsheet for Animal Crossing New Horizons
# https://docs.google.com/spreadsheets/d/13d_LAJPlxMa_DubPTuirkIV4DERBMXbrWQsmSh8ReK4/edit#gid=371893803

class Accessory(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    mannequin_season = models.CharField(db_column='MANNEQUIN_SEASON', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    villager_gender = models.CharField(db_column='VILLAGER_GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_ACCESSORIES'
        verbose_name_plural = 'Accessories'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Achievement(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    achievement_description = models.CharField(db_column='ACHIEVEMENT_DESCRIPTION', max_length=1000, blank=True, null=True)
    achievement_criteria = models.CharField(db_column='ACHIEVEMENT_CRITERIA', max_length=255, blank=True, null=True)
    number = models.CharField(db_column='NUMBER', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    internal_name = models.CharField(db_column='INTERNAL_NAME', max_length=255, blank=True, null=True)
    internal_category = models.CharField(db_column='INTERNAL_CATEGORY', max_length=255, blank=True, null=True)
    num_of_tiers = models.CharField(db_column='NUM_OF_TIERS', max_length=255, blank=True, null=True)
    tier_1 = models.CharField(db_column='TIER_1', max_length=255, blank=True, null=True)
    tier_2 = models.CharField(db_column='TIER_2', max_length=255, blank=True, null=True)
    tier_3 = models.CharField(db_column='TIER_3', max_length=255, blank=True, null=True)
    tier_4 = models.CharField(db_column='TIER_4', max_length=255, blank=True, null=True)
    tier_5 = models.CharField(db_column='TIER_5', max_length=255, blank=True, null=True)
    tier_6 = models.CharField(db_column='TIER_6', max_length=255, blank=True, null=True)
    tier_1_reward = models.CharField(db_column='TIER_1_REWARD', max_length=255, blank=True, null=True)
    tier_2_reward = models.CharField(db_column='TIER_2_REWARD', max_length=255, blank=True, null=True)
    tier_3_reward = models.CharField(db_column='TIER_3_REWARD', max_length=255, blank=True, null=True)
    tier_4_reward = models.CharField(db_column='TIER_4_REWARD', max_length=255, blank=True, null=True)
    tier_5_reward = models.CharField(db_column='TIER_5_REWARD', max_length=255, blank=True, null=True)
    tier_6_reward = models.CharField(db_column='TIER_6_REWARD', max_length=255, blank=True, null=True)
    tier_1_modifier = models.CharField(db_column='TIER_1_MODIFIER', max_length=255, blank=True, null=True)
    tier_1_noun = models.CharField(db_column='TIER_1_NOUN', max_length=255, blank=True, null=True)
    tier_2_modifier = models.CharField(db_column='TIER_2_MODIFIER', max_length=255, blank=True, null=True)
    tier_2_noun = models.CharField(db_column='TIER_2_NOUN', max_length=255, blank=True, null=True)
    tier_3_modifier = models.CharField(db_column='TIER_3_MODIFIER', max_length=255, blank=True, null=True)
    tier_3_noun = models.CharField(db_column='TIER_3_NOUN', max_length=255, blank=True, null=True)
    tier_4_modifier = models.CharField(db_column='TIER_4_MODIFIER', max_length=255, blank=True, null=True)
    tier_4_noun = models.CharField(db_column='TIER_4_NOUN', max_length=255, blank=True, null=True)
    tier_5_modifier = models.CharField(db_column='TIER_5_MODIFIER', max_length=255, blank=True, null=True)
    tier_5_noun = models.CharField(db_column='TIER_5_NOUN', max_length=255, blank=True, null=True)
    tier_6_modifier = models.CharField(db_column='TIER_6_MODIFIER', max_length=255, blank=True, null=True)
    tier_6_noun = models.CharField(db_column='TIER_6_NOUN', max_length=255, blank=True, null=True)
    sequential = models.CharField(db_column='SEQUENTIAL', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_ACHIEVEMENTS'

    def __str__(self):
        return self.name

class Artwork(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    high_res_texture = models.CharField(db_column='HIGH_RES_TEXTURE', max_length=255, blank=True, null=True)
    genuine = models.CharField(db_column='GENUINE', max_length=255, blank=True, null=True)
    category = models.CharField(db_column='CATEGORY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    real_artwork_title = models.CharField(db_column='REAL_ARTWORK_TITLE', max_length=255, blank=True, null=True)
    artist = models.CharField(db_column='ARTIST', max_length=255, blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=1000, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    hha_set = models.CharField(db_column='HHA_SET', max_length=255, blank=True, null=True)
    interact = models.CharField(db_column='INTERACT', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    speaker_type = models.CharField(db_column='SPEAKER_TYPE', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_ARTWORK'
        verbose_name_plural = 'Artwork'

    def __str__(self):
        return self.name + ' (Genuine: ' + self.genuine + ')'

class Bag(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_BAGS'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Bottom(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    mannequin_season = models.CharField(db_column='MANNEQUIN_SEASON', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_BOTTOMS'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class CeilingDecor(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    pattern = models.CharField(db_column='PATTERN', max_length=255, blank=True, null=True)
    pattern_title = models.CharField(db_column='PATTERN_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    body_customize = models.CharField(db_column='BODY_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize = models.CharField(db_column='PATTERN_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize_options = models.CharField(db_column='PATTERN_CUSTOMIZE_OPTIONS', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    kit_type = models.CharField(db_column='KIT_TYPE', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    hha_set = models.CharField(db_column='HHA_SET', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    interact = models.CharField(db_column='INTERACT', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    outdoor = models.CharField(db_column='OUTDOOR', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_CEILING_DECOR'
        verbose_name_plural = 'CeilingDecor'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class ClothingOther(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    primary_shape = models.CharField(db_column='PRIMARY_SHAPE', max_length=255, blank=True, null=True)
    secondary_shape = models.CharField(db_column='SECONDARY_SHAPE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_CLOTHING_OTHER'
        verbose_name_plural = 'ClothingOther'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Construction(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    category = models.CharField(db_column='CATEGORY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_CONSTRUCTION'

    def __str__(self):
        return self.name + ' (' + self.category + ')'

class DressUp(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    mannequin_season = models.CharField(db_column='MANNEQUIN_SEASON', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    villager_gender = models.CharField(db_column='VILLAGER_GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    primary_shape = models.CharField(db_column='PRIMARY_SHAPE', max_length=255, blank=True, null=True)
    secondary_shape = models.CharField(db_column='SECONDARY_SHAPE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_DRESS_UP'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Fencing(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    customize = models.CharField(db_column='CUSTOMIZE', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    kit_type = models.CharField(db_column='KIT_TYPE', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    stack_size = models.CharField(db_column='STACK_SIZE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_FENCING'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Fish(models.Model):
    number = models.CharField(db_column='NUMBER', max_length=255, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    icon_image = models.CharField(db_column='ICON_IMAGE', max_length=255, blank=True, null=True)
    critterpedia_image = models.CharField(db_column='CRITTERPEDIA_IMAGE', max_length=255, blank=True, null=True)
    furniture_image = models.CharField(db_column='FURNITURE_IMAGE', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    where_how = models.CharField(db_column='WHERE_HOW', max_length=255, blank=True, null=True)
    shadow = models.CharField(db_column='SHADOW', max_length=255, blank=True, null=True)
    catch_difficulty = models.CharField(db_column='CATCH_DIFFICULTY', max_length=255, blank=True, null=True)
    vision = models.CharField(db_column='VISION', max_length=255, blank=True, null=True)
    total_catches_to_unlock = models.CharField(db_column='TOTAL_CATCHES_TO_UNLOCK', max_length=255, blank=True, null=True)
    spawn_rates = models.CharField(db_column='SPAWN_RATES', max_length=255, blank=True, null=True)
    nh_jan = models.CharField(db_column='NH_JAN', max_length=255, blank=True, null=True)
    nh_feb = models.CharField(db_column='NH_FEB', max_length=255, blank=True, null=True)
    nh_mar = models.CharField(db_column='NH_MAR', max_length=255, blank=True, null=True)
    nh_apr = models.CharField(db_column='NH_APR', max_length=255, blank=True, null=True)
    nh_may = models.CharField(db_column='NH_MAY', max_length=255, blank=True, null=True)
    nh_jun = models.CharField(db_column='NH_JUN', max_length=255, blank=True, null=True)
    nh_jul = models.CharField(db_column='NH_JUL', max_length=255, blank=True, null=True)
    nh_aug = models.CharField(db_column='NH_AUG', max_length=255, blank=True, null=True)
    nh_sep = models.CharField(db_column='NH_SEP', max_length=255, blank=True, null=True)
    nh_oct = models.CharField(db_column='NH_OCT', max_length=255, blank=True, null=True)
    nh_nov = models.CharField(db_column='NH_NOV', max_length=255, blank=True, null=True)
    nh_dec = models.CharField(db_column='NH_DEC', max_length=255, blank=True, null=True)
    sh_jan = models.CharField(db_column='SH_JAN', max_length=255, blank=True, null=True)
    sh_feb = models.CharField(db_column='SH_FEB', max_length=255, blank=True, null=True)
    sh_mar = models.CharField(db_column='SH_MAR', max_length=255, blank=True, null=True)
    sh_apr = models.CharField(db_column='SH_APR', max_length=255, blank=True, null=True)
    sh_may = models.CharField(db_column='SH_MAY', max_length=255, blank=True, null=True)
    sh_jun = models.CharField(db_column='SH_JUN', max_length=255, blank=True, null=True)
    sh_jul = models.CharField(db_column='SH_JUL', max_length=255, blank=True, null=True)
    sh_aug = models.CharField(db_column='SH_AUG', max_length=255, blank=True, null=True)
    sh_sep = models.CharField(db_column='SH_SEP', max_length=255, blank=True, null=True)
    sh_oct = models.CharField(db_column='SH_OCT', max_length=255, blank=True, null=True)
    sh_nov = models.CharField(db_column='SH_NOV', max_length=255, blank=True, null=True)
    sh_dec = models.CharField(db_column='SH_DEC', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    surface = models.CharField(db_column='SURFACE', max_length=255, blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=1000, blank=True, null=True)
    catch_phrase = models.CharField(db_column='CATCH_PHRASE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    icon_filename = models.CharField(db_column='ICON_FILENAME', max_length=255, blank=True, null=True)
    critterpedia_filename = models.CharField(db_column='CRITTERPEDIA_FILENAME', max_length=255, blank=True, null=True)
    furniture_filename = models.CharField(db_column='FURNITURE_FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_FISH'
        verbose_name_plural = 'Fishes'

    def __str__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    vfx = models.CharField(db_column='VFX', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_FLOORS'

    def __str__(self):
        return self.name

class Fossil(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    fossil_group = models.CharField(db_column='FOSSIL_GROUP', max_length=255, blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=1000, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    museum = models.CharField(db_column='MUSEUM', max_length=255, blank=True, null=True)
    interact = models.CharField(db_column='INTERACT', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_FOSSILS'

    def __str__(self):
        return self.name

class Gyroid(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    pattern = models.CharField(db_column='PATTERN', max_length=255, blank=True, null=True)
    pattern_title = models.CharField(db_column='PATTERN_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    body_customize = models.CharField(db_column='BODY_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize = models.CharField(db_column='PATTERN_CUSTOMIZE', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    kit_type = models.CharField(db_column='KIT_TYPE', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    hha_set = models.CharField(db_column='HHA_SET', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    interact = models.CharField(db_column='INTERACT', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    outdoor = models.CharField(db_column='OUTDOOR', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    sound_type = models.CharField(db_column='SOUND_TYPE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_GYROIDS'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Headwear(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    mannequin_season = models.CharField(db_column='MANNEQUIN_SEASON', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    villager_gender = models.CharField(db_column='VILLAGER_GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_HEADWEAR'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Houseware(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    pattern = models.CharField(db_column='PATTERN', max_length=255, blank=True, null=True)
    pattern_title = models.CharField(db_column='PATTERN_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    body_customize = models.CharField(db_column='BODY_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize = models.CharField(db_column='PATTERN_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize_options = models.CharField(db_column='PATTERN_CUSTOMIZE_OPTIONS', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    kit_type = models.CharField(db_column='KIT_TYPE', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    surface = models.CharField(db_column='SURFACE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    hha_set = models.CharField(db_column='HHA_SET', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    interact = models.CharField(db_column='INTERACT', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    outdoor = models.CharField(db_column='OUTDOOR', max_length=255, blank=True, null=True)
    speaker_type = models.CharField(db_column='SPEAKER_TYPE', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_HOUSEWARES'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Insect(models.Model):
    number = models.CharField(db_column='NUMBER', max_length=255, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    icon_image = models.CharField(db_column='ICON_IMAGE', max_length=255, blank=True, null=True)
    critterpedia_image = models.CharField(db_column='CRITTERPEDIA_IMAGE', max_length=255, blank=True, null=True)
    furniture_image = models.CharField(db_column='FURNITURE_IMAGE', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    where_how = models.CharField(db_column='WHERE_HOW', max_length=255, blank=True, null=True)
    weather = models.CharField(db_column='WEATHER', max_length=255, blank=True, null=True)
    total_catches_to_unlock = models.CharField(db_column='TOTAL_CATCHES_TO_UNLOCK', max_length=255, blank=True, null=True)
    spawn_rates = models.CharField(db_column='SPAWN_RATES', max_length=255, blank=True, null=True)
    nh_jan = models.CharField(db_column='NH_JAN', max_length=255, blank=True, null=True)
    nh_feb = models.CharField(db_column='NH_FEB', max_length=255, blank=True, null=True)
    nh_mar = models.CharField(db_column='NH_MAR', max_length=255, blank=True, null=True)
    nh_apr = models.CharField(db_column='NH_APR', max_length=255, blank=True, null=True)
    nh_may = models.CharField(db_column='NH_MAY', max_length=255, blank=True, null=True)
    nh_jun = models.CharField(db_column='NH_JUN', max_length=255, blank=True, null=True)
    nh_jul = models.CharField(db_column='NH_JUL', max_length=255, blank=True, null=True)
    nh_aug = models.CharField(db_column='NH_AUG', max_length=255, blank=True, null=True)
    nh_sep = models.CharField(db_column='NH_SEP', max_length=255, blank=True, null=True)
    nh_oct = models.CharField(db_column='NH_OCT', max_length=255, blank=True, null=True)
    nh_nov = models.CharField(db_column='NH_NOV', max_length=255, blank=True, null=True)
    nh_dec = models.CharField(db_column='NH_DEC', max_length=255, blank=True, null=True)
    sh_jan = models.CharField(db_column='SH_JAN', max_length=255, blank=True, null=True)
    sh_feb = models.CharField(db_column='SH_FEB', max_length=255, blank=True, null=True)
    sh_mar = models.CharField(db_column='SH_MAR', max_length=255, blank=True, null=True)
    sh_apr = models.CharField(db_column='SH_APR', max_length=255, blank=True, null=True)
    sh_may = models.CharField(db_column='SH_MAY', max_length=255, blank=True, null=True)
    sh_jun = models.CharField(db_column='SH_JUN', max_length=255, blank=True, null=True)
    sh_jul = models.CharField(db_column='SH_JUL', max_length=255, blank=True, null=True)
    sh_aug = models.CharField(db_column='SH_AUG', max_length=255, blank=True, null=True)
    sh_sep = models.CharField(db_column='SH_SEP', max_length=255, blank=True, null=True)
    sh_oct = models.CharField(db_column='SH_OCT', max_length=255, blank=True, null=True)
    sh_nov = models.CharField(db_column='SH_NOV', max_length=255, blank=True, null=True)
    sh_dec = models.CharField(db_column='SH_DEC', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    surface = models.CharField(db_column='SURFACE', max_length=255, blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=1000, blank=True, null=True)
    catch_phrase = models.CharField(db_column='CATCH_PHRASE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    icon_filename = models.CharField(db_column='ICON_FILENAME', max_length=255, blank=True, null=True)
    critterpedia_filename = models.CharField(db_column='CRITTERPEDIA_FILENAME', max_length=255, blank=True, null=True)
    furniture_filename = models.CharField(db_column='FURNITURE_FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_INSECTS'

    def __str__(self):
        return self.name

class InteriorStructure(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    pattern = models.CharField(db_column='PATTERN', max_length=255, blank=True, null=True)
    pattern_title = models.CharField(db_column='PATTERN_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    body_customize = models.CharField(db_column='BODY_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize = models.CharField(db_column='PATTERN_CUSTOMIZE', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    kit_type = models.CharField(db_column='KIT_TYPE', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    surface = models.CharField(db_column='SURFACE', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    hha_set = models.CharField(db_column='HHA_SET', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    interact = models.CharField(db_column='INTERACT', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    outdoor = models.CharField(db_column='OUTDOOR', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_INTERIOR_STRUCTURES'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class MessageCard(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    back_color = models.CharField(db_column='BACK_COLOR', max_length=255, blank=True, null=True)
    body_color = models.CharField(db_column='BODY_COLOR', max_length=255, blank=True, null=True)
    head_color = models.CharField(db_column='HEAD_COLOR', max_length=255, blank=True, null=True)
    foot_color = models.CharField(db_column='FOOT_COLOR', max_length=255, blank=True, null=True)
    pen_color_1 = models.CharField(db_column='PEN_COLOR_1', max_length=255, blank=True, null=True)
    pen_color_2 = models.CharField(db_column='PEN_COLOR_2', max_length=255, blank=True, null=True)
    pen_color_3 = models.CharField(db_column='PEN_COLOR_3', max_length=255, blank=True, null=True)
    pen_color_4 = models.CharField(db_column='PEN_COLOR_4', max_length=255, blank=True, null=True)
    start_date = models.CharField(db_column='START_DATE', max_length=255, blank=True, null=True)
    end_date = models.CharField(db_column='END_DATE', max_length=255, blank=True, null=True)
    nh_start_date = models.CharField(db_column='NH_START_DATE', max_length=255, blank=True, null=True)
    nh_end_date = models.CharField(db_column='NH_END_DATE', max_length=255, blank=True, null=True)
    sh_start_date = models.CharField(db_column='SH_START_DATE', max_length=255, blank=True, null=True)
    sh_end_date = models.CharField(db_column='SH_END_DATE', max_length=255, blank=True, null=True)
    version = models.CharField(db_column='VERSION', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_MESSAGE_CARDS'

    def __str__(self):
        return self.name

class Miscellaneous(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    pattern = models.CharField(db_column='PATTERN', max_length=255, blank=True, null=True)
    pattern_title = models.CharField(db_column='PATTERN_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    body_customize = models.CharField(db_column='BODY_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize = models.CharField(db_column='PATTERN_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize_options = models.CharField(db_column='PATTERN_CUSTOMIZE_OPTIONS', max_length=255, blank=True, null=True)
    stack_size = models.CharField(db_column='STACK_SIZE', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    kit_type = models.CharField(db_column='KIT_TYPE', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    surface = models.CharField(db_column='SURFACE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    hha_set = models.CharField(db_column='HHA_SET', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    interact = models.CharField(db_column='INTERACT', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    outdoor = models.CharField(db_column='OUTDOOR', max_length=255, blank=True, null=True)
    speaker_type = models.CharField(db_column='SPEAKER_TYPE', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    food_power = models.CharField(db_column='FOOD_POWER', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_MISCELLANEOUS'
        verbose_name_plural = 'Miscellaneous'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Music(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    framed_image = models.CharField(db_column='FRAMED_IMAGE', max_length=255, blank=True, null=True)
    album_image = models.CharField(db_column='ALBUM_IMAGE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_MUSIC'
        verbose_name_plural = 'Music'

    def __str__(self):
        return self.name

class Other(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    inventory_image = models.CharField(db_column='INVENTORY_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    stack_size = models.CharField(db_column='STACK_SIZE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    food_power = models.CharField(db_column='FOOD_POWER', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    inventory_filename = models.CharField(db_column='INVENTORY_FILENAME', max_length=255, blank=True, null=True)
    storage_filename = models.CharField(db_column='STORAGE_FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_OTHER'

    def __str__(self):
        return self.name

class ParadisePlanning(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    request = models.CharField(db_column='REQUEST', max_length=255, blank=True, null=True)
    thought_bubble = models.CharField(db_column='THOUGHT_BUBBLE', max_length=255, blank=True, null=True)
    song = models.CharField(db_column='SONG', max_length=255, blank=True, null=True)
    furniture_list = models.CharField(db_column='FURNITURE_LIST', max_length=1000, blank=True, null=True)
    furniture_name_list = models.CharField(db_column='FURNITURE_NAME_LIST', max_length=1000, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_PARADISE_PLANNING'

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    pattern = models.CharField(db_column='PATTERN', max_length=255, blank=True, null=True)
    pattern_title = models.CharField(db_column='PATTERN_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    customize = models.CharField(db_column='CUSTOMIZE', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_PHOTOS'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Poster(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_POSTERS'

    def __str__(self):
        return self.name

class Reaction(models.Model):
    number = models.CharField(db_column='NUMBER', max_length=255, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    icon_filename = models.CharField(db_column='ICON_FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_REACTIONS'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    image_sh = models.CharField(db_column='IMAGE_SH', max_length=255, blank=True, null=True)
    number_1 = models.CharField(db_column='NUMBER_1', max_length=255, blank=True, null=True)
    material_1 = models.CharField(db_column='MATERIAL_1', max_length=255, blank=True, null=True)
    number_2 = models.CharField(db_column='NUMBER_2', max_length=255, blank=True, null=True)
    material_2 = models.CharField(db_column='MATERIAL_2', max_length=255, blank=True, null=True)
    number_3 = models.CharField(db_column='NUMBER_3', max_length=255, blank=True, null=True)
    material_3 = models.CharField(db_column='MATERIAL_3', max_length=255, blank=True, null=True)
    number_4 = models.CharField(db_column='NUMBER_4', max_length=255, blank=True, null=True)
    material_4 = models.CharField(db_column='MATERIAL_4', max_length=255, blank=True, null=True)
    number_5 = models.CharField(db_column='NUMBER_5', max_length=255, blank=True, null=True)
    material_5 = models.CharField(db_column='MATERIAL_5', max_length=255, blank=True, null=True)
    number_6 = models.CharField(db_column='NUMBER_6', max_length=255, blank=True, null=True)
    material_6 = models.CharField(db_column='MATERIAL_6', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    recipes_to_unlock = models.CharField(db_column='RECIPES_TO_UNLOCK', max_length=255, blank=True, null=True)
    category = models.CharField(db_column='CATEGORY', max_length=255, blank=True, null=True)
    crafted_item_internal_id = models.CharField(db_column='CRAFTED_ITEM_INTERNAL_ID', max_length=255, blank=True, null=True)
    card_color = models.CharField(db_column='CARD_COLOR', max_length=255, blank=True, null=True)
    diy_icon_filename = models.CharField(db_column='DIY_ICON_FILENAME', max_length=255, blank=True, null=True)
    diy_icon_filename_sh = models.CharField(db_column='DIY_ICON_FILENAME_SH', max_length=255, blank=True, null=True)
    serial_id = models.CharField(db_column='SERIAL_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_RECIPES'

    def __str__(self):
        return self.name

class Rug(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    size_category = models.CharField(db_column='SIZE_CATEGORY', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_RUGS'

    def __str__(self):
        return self.name

class SeasonEvent(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)
    display_name = models.CharField(db_column='DISPLAY_NAME', max_length=255, blank=True, null=True)
    number_2022_nh = models.CharField(db_column='2022_NH', max_length=20, blank=True, null=True)
    number_2022_sh = models.CharField(db_column='2022_SH', max_length=20, blank=True, null=True)
    number_2023_nh = models.CharField(db_column='2023_NH', max_length=20, blank=True, null=True)
    number_2023_sh = models.CharField(db_column='2023_SH', max_length=20, blank=True, null=True)
    number_2024_nh = models.CharField(db_column='2024_NH', max_length=20, blank=True, null=True)
    number_2024_sh = models.CharField(db_column='2024_SH', max_length=20, blank=True, null=True)
    sort_date = models.CharField(db_column='SORT_DATE', max_length=255, blank=True, null=True)
    date_varies_by_year = models.CharField(db_column='DATE_VARIES_BY_YEAR', max_length=255, blank=True, null=True)
    start_time = models.CharField(db_column='START_TIME', max_length=255, blank=True, null=True)
    end_time = models.CharField(db_column='END_TIME', max_length=255, blank=True, null=True)
    next_day_overlap = models.CharField(db_column='NEXT_DAY_OVERLAP', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    version_last_updated = models.CharField(db_column='VERSION_LAST_UPDATED', max_length=255, blank=True, null=True)
    internal_label = models.CharField(db_column='INTERNAL_LABEL', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)
    year_2000_nh = models.CharField(db_column='2000_NH', max_length=20, blank=True, null=True)
    year_2000_sh = models.CharField(db_column='2000_SH', max_length=20, blank=True, null=True)
    year_2001_nh = models.CharField(db_column='2001_NH', max_length=20, blank=True, null=True)
    year_2001_sh = models.CharField(db_column='2001_SH', max_length=20, blank=True, null=True)
    year_2002_nh = models.CharField(db_column='2002_NH', max_length=20, blank=True, null=True)
    year_2002_sh = models.CharField(db_column='2002_SH', max_length=20, blank=True, null=True)
    year_2003_nh = models.CharField(db_column='2003_NH', max_length=20, blank=True, null=True)
    year_2003_sh = models.CharField(db_column='2003_SH', max_length=20, blank=True, null=True)
    year_2004_nh = models.CharField(db_column='2004_NH', max_length=20, blank=True, null=True)
    year_2004_sh = models.CharField(db_column='2004_SH', max_length=20, blank=True, null=True)
    year_2005_nh = models.CharField(db_column='2005_NH', max_length=20, blank=True, null=True)
    year_2005_sh = models.CharField(db_column='2005_SH', max_length=20, blank=True, null=True)
    year_2006_nh = models.CharField(db_column='2006_NH', max_length=20, blank=True, null=True)
    year_2006_sh = models.CharField(db_column='2006_SH', max_length=20, blank=True, null=True)
    year_2007_nh = models.CharField(db_column='2007_NH', max_length=20, blank=True, null=True)
    year_2007_sh = models.CharField(db_column='2007_SH', max_length=20, blank=True, null=True)
    year_2008_nh = models.CharField(db_column='2008_NH', max_length=20, blank=True, null=True)
    year_2008_sh = models.CharField(db_column='2008_SH', max_length=20, blank=True, null=True)
    year_2009_nh = models.CharField(db_column='2009_NH', max_length=20, blank=True, null=True)
    year_2009_sh = models.CharField(db_column='2009_SH', max_length=20, blank=True, null=True)
    year_2010_nh = models.CharField(db_column='2010_NH', max_length=20, blank=True, null=True)
    year_2010_sh = models.CharField(db_column='2010_SH', max_length=20, blank=True, null=True)
    year_2011_nh = models.CharField(db_column='2011_NH', max_length=20, blank=True, null=True)
    year_2011_sh = models.CharField(db_column='2011_SH', max_length=20, blank=True, null=True)
    year_2012_nh = models.CharField(db_column='2012_NH', max_length=20, blank=True, null=True)
    year_2012_sh = models.CharField(db_column='2012_SH', max_length=20, blank=True, null=True)
    year_2013_nh = models.CharField(db_column='2013_NH', max_length=20, blank=True, null=True)
    year_2013_sh = models.CharField(db_column='2013_SH', max_length=20, blank=True, null=True)
    year_2014_nh = models.CharField(db_column='2014_NH', max_length=20, blank=True, null=True)
    year_2014_sh = models.CharField(db_column='2014_SH', max_length=20, blank=True, null=True)
    year_2015_nh = models.CharField(db_column='2015_NH', max_length=20, blank=True, null=True)
    year_2015_sh = models.CharField(db_column='2015_SH', max_length=20, blank=True, null=True)
    year_2016_nh = models.CharField(db_column='2016_NH', max_length=20, blank=True, null=True)
    year_2016_sh = models.CharField(db_column='2016_SH', max_length=20, blank=True, null=True)
    year_2017_nh = models.CharField(db_column='2017_NH', max_length=20, blank=True, null=True)
    year_2017_sh = models.CharField(db_column='2017_SH', max_length=20, blank=True, null=True)
    year_2018_nh = models.CharField(db_column='2018_NH', max_length=20, blank=True, null=True)
    year_2018_sh = models.CharField(db_column='2018_SH', max_length=20, blank=True, null=True)
    year_2019_nh = models.CharField(db_column='2019_NH', max_length=20, blank=True, null=True)
    year_2019_sh = models.CharField(db_column='2019_SH', max_length=20, blank=True, null=True)
    year_2020_nh = models.CharField(db_column='2020_NH', max_length=20, blank=True, null=True)
    year_2020_sh = models.CharField(db_column='2020_SH', max_length=20, blank=True, null=True)
    year_2021_nh = models.CharField(db_column='2021_NH', max_length=20, blank=True, null=True)
    year_2021_sh = models.CharField(db_column='2021_SH', max_length=20, blank=True, null=True)
    year_2025_nh = models.CharField(db_column='2025_NH', max_length=20, blank=True, null=True)
    year_2025_sh = models.CharField(db_column='2025_SH', max_length=20, blank=True, null=True)
    year_2026_nh = models.CharField(db_column='2026_NH', max_length=20, blank=True, null=True)
    year_2026_sh = models.CharField(db_column='2026_SH', max_length=20, blank=True, null=True)
    year_2027_nh = models.CharField(db_column='2027_NH', max_length=20, blank=True, null=True)
    year_2027_sh = models.CharField(db_column='2027_SH', max_length=20, blank=True, null=True)
    year_2028_nh = models.CharField(db_column='2028_NH', max_length=20, blank=True, null=True)
    year_2028_sh = models.CharField(db_column='2028_SH', max_length=20, blank=True, null=True)
    year_2029_nh = models.CharField(db_column='2029_NH', max_length=20, blank=True, null=True)
    year_2029_sh = models.CharField(db_column='2029_SH', max_length=20, blank=True, null=True)
    year_2030_nh = models.CharField(db_column='2030_NH', max_length=20, blank=True, null=True)
    year_2030_sh = models.CharField(db_column='2030_SH', max_length=20, blank=True, null=True)
    year_2031_nh = models.CharField(db_column='2031_NH', max_length=20, blank=True, null=True)
    year_2031_sh = models.CharField(db_column='2031_SH', max_length=20, blank=True, null=True)
    year_2032_nh = models.CharField(db_column='2032_NH', max_length=20, blank=True, null=True)
    year_2032_sh = models.CharField(db_column='2032_SH', max_length=20, blank=True, null=True)
    year_2033_nh = models.CharField(db_column='2033_NH', max_length=20, blank=True, null=True)
    year_2033_sh = models.CharField(db_column='2033_SH', max_length=20, blank=True, null=True)
    year_2034_nh = models.CharField(db_column='2034_NH', max_length=20, blank=True, null=True)
    year_2034_sh = models.CharField(db_column='2034_SH', max_length=20, blank=True, null=True)
    year_2035_nh = models.CharField(db_column='2035_NH', max_length=20, blank=True, null=True)
    year_2035_sh = models.CharField(db_column='2035_SH', max_length=20, blank=True, null=True)
    year_2036_nh = models.CharField(db_column='2036_NH', max_length=20, blank=True, null=True)
    year_2036_sh = models.CharField(db_column='2036_SH', max_length=20, blank=True, null=True)
    year_2037_nh = models.CharField(db_column='2037_NH', max_length=20, blank=True, null=True)
    year_2037_sh = models.CharField(db_column='2037_SH', max_length=20, blank=True, null=True)
    year_2038_nh = models.CharField(db_column='2038_NH', max_length=20, blank=True, null=True)
    year_2038_sh = models.CharField(db_column='2038_SH', max_length=20, blank=True, null=True)
    year_2039_nh = models.CharField(db_column='2039_NH', max_length=20, blank=True, null=True)
    year_2039_sh = models.CharField(db_column='2039_SH', max_length=20, blank=True, null=True)
    year_2040_nh = models.CharField(db_column='2040_NH', max_length=20, blank=True, null=True)
    year_2040_sh = models.CharField(db_column='2040_SH', max_length=20, blank=True, null=True)
    year_2041_nh = models.CharField(db_column='2041_NH', max_length=20, blank=True, null=True)
    year_2041_sh = models.CharField(db_column='2041_SH', max_length=20, blank=True, null=True)
    year_2042_nh = models.CharField(db_column='2042_NH', max_length=20, blank=True, null=True)
    year_2042_sh = models.CharField(db_column='2042_SH', max_length=20, blank=True, null=True)
    year_2043_nh = models.CharField(db_column='2043_NH', max_length=20, blank=True, null=True)
    year_2043_sh = models.CharField(db_column='2043_SH', max_length=20, blank=True, null=True)
    year_2044_nh = models.CharField(db_column='2044_NH', max_length=20, blank=True, null=True)
    year_2044_sh = models.CharField(db_column='2044_SH', max_length=20, blank=True, null=True)
    year_2045_nh = models.CharField(db_column='2045_NH', max_length=20, blank=True, null=True)
    year_2045_sh = models.CharField(db_column='2045_SH', max_length=20, blank=True, null=True)
    year_2046_nh = models.CharField(db_column='2046_NH', max_length=20, blank=True, null=True)
    year_2046_sh = models.CharField(db_column='2046_SH', max_length=20, blank=True, null=True)
    year_2047_nh = models.CharField(db_column='2047_NH', max_length=20, blank=True, null=True)
    year_2047_sh = models.CharField(db_column='2047_SH', max_length=20, blank=True, null=True)
    year_2048_nh = models.CharField(db_column='2048_NH', max_length=20, blank=True, null=True)
    year_2048_sh = models.CharField(db_column='2048_SH', max_length=20, blank=True, null=True)
    year_2049_nh = models.CharField(db_column='2049_NH', max_length=20, blank=True, null=True)
    year_2049_sh = models.CharField(db_column='2049_SH', max_length=20, blank=True, null=True)
    year_2050_nh = models.CharField(db_column='2050_NH', max_length=20, blank=True, null=True)
    year_2050_sh = models.CharField(db_column='2050_SH', max_length=20, blank=True, null=True)
    year_2051_nh = models.CharField(db_column='2051_NH', max_length=20, blank=True, null=True)
    year_2051_sh = models.CharField(db_column='2051_SH', max_length=20, blank=True, null=True)
    year_2052_nh = models.CharField(db_column='2052_NH', max_length=20, blank=True, null=True)
    year_2052_sh = models.CharField(db_column='2052_SH', max_length=20, blank=True, null=True)
    year_2053_nh = models.CharField(db_column='2053_NH', max_length=20, blank=True, null=True)
    year_2053_sh = models.CharField(db_column='2053_SH', max_length=20, blank=True, null=True)
    year_2054_nh = models.CharField(db_column='2054_NH', max_length=20, blank=True, null=True)
    year_2054_sh = models.CharField(db_column='2054_SH', max_length=20, blank=True, null=True)
    year_2055_nh = models.CharField(db_column='2055_NH', max_length=20, blank=True, null=True)
    year_2055_sh = models.CharField(db_column='2055_SH', max_length=20, blank=True, null=True)
    year_2056_nh = models.CharField(db_column='2056_NH', max_length=20, blank=True, null=True)
    year_2056_sh = models.CharField(db_column='2056_SH', max_length=20, blank=True, null=True)
    year_2057_nh = models.CharField(db_column='2057_NH', max_length=20, blank=True, null=True)
    year_2057_sh = models.CharField(db_column='2057_SH', max_length=20, blank=True, null=True)
    year_2058_nh = models.CharField(db_column='2058_NH', max_length=20, blank=True, null=True)
    year_2058_sh = models.CharField(db_column='2058_SH', max_length=20, blank=True, null=True)
    year_2059_nh = models.CharField(db_column='2059_NH', max_length=20, blank=True, null=True)
    year_2059_sh = models.CharField(db_column='2059_SH', max_length=20, blank=True, null=True)
    year_2060_nh = models.CharField(db_column='2060_NH', max_length=20, blank=True, null=True)
    year_2060_sh = models.CharField(db_column='2060_SH', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_SEASONS_AND_EVENTS'
        verbose_name_plural = 'SeasonsAndEvents'

    def __str__(self):
        return self.name + ' (' + self.type + ', ' + self.sort_date + ')'

class SeaCreature(models.Model):
    number = models.CharField(db_column='NUMBER', max_length=255, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    icon_image = models.CharField(db_column='ICON_IMAGE', max_length=255, blank=True, null=True)
    critterpedia_image = models.CharField(db_column='CRITTERPEDIA_IMAGE', max_length=255, blank=True, null=True)
    furniture_image = models.CharField(db_column='FURNITURE_IMAGE', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    shadow = models.CharField(db_column='SHADOW', max_length=255, blank=True, null=True)
    movement_speed = models.CharField(db_column='MOVEMENT_SPEED', max_length=255, blank=True, null=True)
    total_catches_to_unlock = models.CharField(db_column='TOTAL_CATCHES_TO_UNLOCK', max_length=255, blank=True, null=True)
    spawn_rates = models.CharField(db_column='SPAWN_RATES', max_length=255, blank=True, null=True)
    nh_jan = models.CharField(db_column='NH_JAN', max_length=255, blank=True, null=True)
    nh_feb = models.CharField(db_column='NH_FEB', max_length=255, blank=True, null=True)
    nh_mar = models.CharField(db_column='NH_MAR', max_length=255, blank=True, null=True)
    nh_apr = models.CharField(db_column='NH_APR', max_length=255, blank=True, null=True)
    nh_may = models.CharField(db_column='NH_MAY', max_length=255, blank=True, null=True)
    nh_jun = models.CharField(db_column='NH_JUN', max_length=255, blank=True, null=True)
    nh_jul = models.CharField(db_column='NH_JUL', max_length=255, blank=True, null=True)
    nh_aug = models.CharField(db_column='NH_AUG', max_length=255, blank=True, null=True)
    nh_sep = models.CharField(db_column='NH_SEP', max_length=255, blank=True, null=True)
    nh_oct = models.CharField(db_column='NH_OCT', max_length=255, blank=True, null=True)
    nh_nov = models.CharField(db_column='NH_NOV', max_length=255, blank=True, null=True)
    nh_dec = models.CharField(db_column='NH_DEC', max_length=255, blank=True, null=True)
    sh_jan = models.CharField(db_column='SH_JAN', max_length=255, blank=True, null=True)
    sh_feb = models.CharField(db_column='SH_FEB', max_length=255, blank=True, null=True)
    sh_mar = models.CharField(db_column='SH_MAR', max_length=255, blank=True, null=True)
    sh_apr = models.CharField(db_column='SH_APR', max_length=255, blank=True, null=True)
    sh_may = models.CharField(db_column='SH_MAY', max_length=255, blank=True, null=True)
    sh_jun = models.CharField(db_column='SH_JUN', max_length=255, blank=True, null=True)
    sh_jul = models.CharField(db_column='SH_JUL', max_length=255, blank=True, null=True)
    sh_aug = models.CharField(db_column='SH_AUG', max_length=255, blank=True, null=True)
    sh_sep = models.CharField(db_column='SH_SEP', max_length=255, blank=True, null=True)
    sh_oct = models.CharField(db_column='SH_OCT', max_length=255, blank=True, null=True)
    sh_nov = models.CharField(db_column='SH_NOV', max_length=255, blank=True, null=True)
    sh_dec = models.CharField(db_column='SH_DEC', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    surface = models.CharField(db_column='SURFACE', max_length=255, blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=1000, blank=True, null=True)
    catch_phrase = models.CharField(db_column='CATCH_PHRASE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    icon_filename = models.CharField(db_column='ICON_FILENAME', max_length=255, blank=True, null=True)
    critterpedia_filename = models.CharField(db_column='CRITTERPEDIA_FILENAME', max_length=255, blank=True, null=True)
    furniture_filename = models.CharField(db_column='FURNITURE_FILENAME', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_SEA_CREATURES'

    def __str__(self):
        return self.name

class Shoes(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    mannequin_season = models.CharField(db_column='MANNEQUIN_SEASON', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_SHOES'
        verbose_name_plural = 'Shoes'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Socks(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    mannequin_season = models.CharField(db_column='MANNEQUIN_SEASON', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_SOCKS'
        verbose_name_plural = 'Socks'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class SpecialNpc(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    icon_image = models.CharField(db_column='ICON_IMAGE', max_length=255, blank=True, null=True)
    photo_image = models.CharField(db_column='PHOTO_IMAGE', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    gender_asia = models.CharField(db_column='GENDER_ASIA', max_length=255, blank=True, null=True)
    hobby = models.CharField(db_column='HOBBY', max_length=255, blank=True, null=True)
    birthday = models.CharField(db_column='BIRTHDAY', max_length=255, blank=True, null=True)
    umbrella = models.CharField(db_column='UMBRELLA', max_length=255, blank=True, null=True)
    umbrella_hhp = models.CharField(db_column='UMBRELLA_HHP', max_length=255, blank=True, null=True)
    name_color = models.CharField(db_column='NAME_COLOR', max_length=255, blank=True, null=True)
    bubble_color = models.CharField(db_column='BUBBLE_COLOR', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    icon_filename = models.CharField(db_column='ICON_FILENAME', max_length=255, blank=True, null=True)
    photo_filename = models.CharField(db_column='PHOTO_FILENAME', max_length=255, blank=True, null=True)
    npc_id = models.CharField(db_column='NPC_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_SPECIAL_NPCS'

    def __str__(self):
        return self.name + ' (' + self.gender + ')'

class ToolGood(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    customize = models.CharField(db_column='CUSTOMIZE', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    kit_type = models.CharField(db_column='KIT_TYPE', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    uses = models.CharField(db_column='USES', max_length=255, blank=True, null=True)
    stack_size = models.CharField(db_column='STACK_SIZE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    in_set = models.CharField(db_column='IN_SET', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    food_power = models.CharField(db_column='FOOD_POWER', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_TOOLS_GOODS'
        verbose_name_plural = 'ToolsGoods'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Top(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    closet_image = models.CharField(db_column='CLOSET_IMAGE', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    seasonal_availability = models.CharField(db_column='SEASONAL_AVAILABILITY', max_length=255, blank=True, null=True)
    seasonality = models.CharField(db_column='SEASONALITY', max_length=255, blank=True, null=True)
    mannequin_season = models.CharField(db_column='MANNEQUIN_SEASON', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    villager_gender = models.CharField(db_column='VILLAGER_GENDER', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    label_themes = models.CharField(db_column='LABEL_THEMES', max_length=255, blank=True, null=True)
    sort_order = models.CharField(db_column='SORT_ORDER', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    clothgroup_id = models.CharField(db_column='CLOTHGROUP_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_TOPS'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'

class Umbrella(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    storage_image = models.CharField(db_column='STORAGE_IMAGE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    villager_gender = models.CharField(db_column='VILLAGER_GENDER', max_length=255, blank=True, null=True)
    villager_equippable = models.CharField(db_column='VILLAGER_EQUIPPABLE', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_UMBRELLAS'

    def __str__(self):
        return self.name

class Villager(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    icon_image = models.CharField(db_column='ICON_IMAGE', max_length=255, blank=True, null=True)
    photo_image = models.CharField(db_column='PHOTO_IMAGE', max_length=255, blank=True, null=True)
    house_image = models.CharField(db_column='HOUSE_IMAGE', max_length=255, blank=True, null=True)
    species = models.CharField(db_column='SPECIES', max_length=255, blank=True, null=True)
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)
    personality = models.CharField(db_column='PERSONALITY', max_length=255, blank=True, null=True)
    subtype = models.CharField(db_column='SUBTYPE', max_length=255, blank=True, null=True)
    hobby = models.CharField(db_column='HOBBY', max_length=255, blank=True, null=True)
    birthday = models.CharField(db_column='BIRTHDAY', max_length=255, blank=True, null=True)
    catchphrase = models.CharField(db_column='CATCHPHRASE', max_length=255, blank=True, null=True)
    favorite_song = models.CharField(db_column='FAVORITE_SONG', max_length=255, blank=True, null=True)
    favorite_saying = models.CharField(db_column='FAVORITE_SAYING', max_length=255, blank=True, null=True)
    style_1 = models.CharField(db_column='STYLE_1', max_length=255, blank=True, null=True)
    style_2 = models.CharField(db_column='STYLE_2', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    default_clothing = models.CharField(db_column='DEFAULT_CLOTHING', max_length=255, blank=True, null=True)
    default_umbrella = models.CharField(db_column='DEFAULT_UMBRELLA', max_length=255, blank=True, null=True)
    wallpaper = models.CharField(db_column='WALLPAPER', max_length=255, blank=True, null=True)
    flooring = models.CharField(db_column='FLOORING', max_length=255, blank=True, null=True)
    furniture_list = models.CharField(db_column='FURNITURE_LIST', max_length=1000, blank=True, null=True)
    furniture_name_list = models.CharField(db_column='FURNITURE_NAME_LIST', max_length=1000, blank=True, null=True)
    diy_workbench = models.CharField(db_column='DIY_WORKBENCH', max_length=255, blank=True, null=True)
    kitchen_equipment = models.CharField(db_column='KITCHEN_EQUIPMENT', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    name_color = models.CharField(db_column='NAME_COLOR', max_length=255, blank=True, null=True)
    bubble_color = models.CharField(db_column='BUBBLE_COLOR', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_VILLAGERS'

    def __str__(self):
        return self.name + ' (' + self.species + ', ' + self.personality + ')'

class Wallpaper(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    vfx = models.CharField(db_column='VFX', max_length=255, blank=True, null=True)
    vfx_type = models.CharField(db_column='VFX_TYPE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    window_type = models.CharField(db_column='WINDOW_TYPE', max_length=255, blank=True, null=True)
    window_color = models.CharField(db_column='WINDOW_COLOR', max_length=255, blank=True, null=True)
    pane_type = models.CharField(db_column='PANE_TYPE', max_length=255, blank=True, null=True)
    curtain_type = models.CharField(db_column='CURTAIN_TYPE', max_length=255, blank=True, null=True)
    curtain_color = models.CharField(db_column='CURTAIN_COLOR', max_length=255, blank=True, null=True)
    ceiling_type = models.CharField(db_column='CEILING_TYPE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_WALLPAPER'

    def __str__(self):
        return self.name

class WallMounted(models.Model):
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)
    variation = models.CharField(db_column='VARIATION', max_length=255, blank=True, null=True)
    body_title = models.CharField(db_column='BODY_TITLE', max_length=255, blank=True, null=True)
    pattern = models.CharField(db_column='PATTERN', max_length=255, blank=True, null=True)
    pattern_title = models.CharField(db_column='PATTERN_TITLE', max_length=255, blank=True, null=True)
    diy = models.CharField(db_column='DIY', max_length=255, blank=True, null=True)
    body_customize = models.CharField(db_column='BODY_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize = models.CharField(db_column='PATTERN_CUSTOMIZE', max_length=255, blank=True, null=True)
    pattern_customize_options = models.CharField(db_column='PATTERN_CUSTOMIZE_OPTIONS', max_length=255, blank=True, null=True)
    kit_cost = models.CharField(db_column='KIT_COST', max_length=255, blank=True, null=True)
    kit_type = models.CharField(db_column='KIT_TYPE', max_length=255, blank=True, null=True)
    cyrus_customize_price = models.CharField(db_column='CYRUS_CUSTOMIZE_PRICE', max_length=255, blank=True, null=True)
    buy = models.CharField(db_column='BUY', max_length=255, blank=True, null=True)
    sell = models.CharField(db_column='SELL', max_length=255, blank=True, null=True)
    color_1 = models.CharField(db_column='COLOR_1', max_length=255, blank=True, null=True)
    color_2 = models.CharField(db_column='COLOR_2', max_length=255, blank=True, null=True)
    exchange_price = models.CharField(db_column='EXCHANGE_PRICE', max_length=255, blank=True, null=True)
    exchange_currency = models.CharField(db_column='EXCHANGE_CURRENCY', max_length=255, blank=True, null=True)
    size = models.CharField(db_column='SIZE', max_length=255, blank=True, null=True)
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)
    source_notes = models.CharField(db_column='SOURCE_NOTES', max_length=1000, blank=True, null=True)
    season_event = models.CharField(db_column='SEASON_EVENT', max_length=255, blank=True, null=True)
    season_event_exclusive = models.CharField(db_column='SEASON_EVENT_EXCLUSIVE', max_length=255, blank=True, null=True)
    hha_base_points = models.CharField(db_column='HHA_BASE_POINTS', max_length=255, blank=True, null=True)
    hha_concept_1 = models.CharField(db_column='HHA_CONCEPT_1', max_length=255, blank=True, null=True)
    hha_concept_2 = models.CharField(db_column='HHA_CONCEPT_2', max_length=255, blank=True, null=True)
    hha_series = models.CharField(db_column='HHA_SERIES', max_length=255, blank=True, null=True)
    hha_set = models.CharField(db_column='HHA_SET', max_length=255, blank=True, null=True)
    hha_category = models.CharField(db_column='HHA_CATEGORY', max_length=255, blank=True, null=True)
    interact = models.CharField(db_column='INTERACT', max_length=255, blank=True, null=True)
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)
    outdoor = models.CharField(db_column='OUTDOOR', max_length=255, blank=True, null=True)
    lighting_type = models.CharField(db_column='LIGHTING_TYPE', max_length=255, blank=True, null=True)
    door_deco = models.CharField(db_column='DOOR_DECO', max_length=255, blank=True, null=True)
    catalog = models.CharField(db_column='CATALOG', max_length=255, blank=True, null=True)
    version_added = models.CharField(db_column='VERSION_ADDED', max_length=255, blank=True, null=True)
    unlocked = models.CharField(db_column='UNLOCKED', max_length=255, blank=True, null=True)
    filename = models.CharField(db_column='FILENAME', max_length=255, blank=True, null=True)
    variant_id = models.CharField(db_column='VARIANT_ID', max_length=255, blank=True, null=True)
    internal_id = models.CharField(db_column='INTERNAL_ID', max_length=255, blank=True, null=True)
    unique_entry_id = models.CharField(db_column='UNIQUE_ENTRY_ID', max_length=255, blank=True, primary_key=True)

    class Meta:
        db_table = 'SHEETS_ITEMS_WALL_MOUNTED'

    def __str__(self):
        return self.name + ' (' + self.variation + ')'