from rest_framework import serializers

from models import *
# This is an example of how you can make your own serializer. Default seems to be working.
# Left this only for examples.

class AcctaxSerializer(serializers.HyperlinkedModelSerializer):
    family = serializers.SlugRelatedField(slug_field='family')
    class Meta:
        model = Acctax
	fields = ('url','a_id','acode','sname','scientificnameauthorship','family','genus','species','subspecies','variety','forma','elcode','gelcode','iucncode','g_rank','s_rank','nativity','source','usda_code','tsn','fed_status','st_status','swap','scientificname','sspscientificnameauthorship','varscientificnameauthorship','formascientificnameauthorship','tracked')

class ComtaxSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer):
    primary_name = serializers.CharField(source='primary_name')
    class Meta:
        model= Comtax
        fields = ['url','c_id','acode','vernacularname','primary_name']

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('url','source', 'description')

class HightaxSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="obis:hightax-detail")
    family = serializers.CharField(source='family')
    class Meta:
         model = Hightax
         fields = ('url','kingdom','phylum','taxclass','taxorder','family','category')

class SyntaxSerializer(serializers.HyperlinkedModelSerializer):    
     class Meta:
         model = Syntax
         fields = ('url','s_id','acode','scode','sname','scientificnameauthorship','family','genus','species','subspecies','variety','scientificname','sspscientificnameauthorship','varscientificnameauthorship','formascientificnameauthorship','tsn')
