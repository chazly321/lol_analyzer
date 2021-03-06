from django.db import models
from heroes.models import Hero

# Create your models here.

class ItemTag(models.Model):
    tag = models.CharField(max_length = 20)

    def __unicode__(self):
        return unicode(str(self.tag))    

class Item(models.Model):
    name = models.CharField(max_length = 50)
    riot_id = models.IntegerField()
    tag = models.ManyToManyField(ItemTag)
    image = models.CharField(max_length = 1000)
    FlatArmorMod = models.IntegerField(default = 0, blank = True, null = True)  
    FlatAttackSpeedMod = models.IntegerField(default = 0, blank = True, null = True)   
    FlatBlockMod = models.IntegerField(default = 0, blank = True, null = True)     
    FlatCritChanceMod = models.FloatField(default = 0, blank = True, null = True)    
    FlatCritDamageMod = models.IntegerField(default = 0, blank = True, null = True)    
    FlatEXPBonus = models.IntegerField(default = 0, blank = True, null = True)     
    FlatEnergyPoolMod = models.IntegerField(default = 0, blank = True, null = True)    
    FlatEnergyRegenMod = models.IntegerField(default = 0, blank = True, null = True)   
    FlatHPPoolMod = models.IntegerField(default = 0, blank = True, null = True)    
    FlatHPRegenMod = models.IntegerField(default = 0, blank = True, null = True)   
    FlatMPPoolMod = models.IntegerField(default = 0, blank = True, null = True)    
    FlatMPRegenMod = models.IntegerField(default = 0, blank = True, null = True)   
    FlatMagicDamageMod = models.IntegerField(default = 0, blank = True, null = True)   
    FlatMovementSpeedMod = models.IntegerField(default = 0, blank = True, null = True)     
    FlatPhysicalDamageMod = models.IntegerField(default = 0, blank = True, null = True)    
    FlatSpellBlockMod = models.IntegerField(default = 0, blank = True, null = True)    
    PercentArmorMod = models.IntegerField(default = 0, blank = True, null = True)  
    PercentAttackSpeedMod = models.IntegerField(default = 0, blank = True, null = True)    
    PercentBlockMod = models.IntegerField(default = 0, blank = True, null = True)  
    PercentCritChanceMod = models.FloatField(default = 0, blank = True, null = True)     
    PercentCritDamageMod = models.FloatField(default = 0, blank = True, null = True)    
    PercentDodgeMod = models.FloatField(default = 0, blank = True, null = True)
    PercentEXPBonus = models.FloatField(default = 0, blank = True, null = True)  
    PercentHPPoolMod = models.FloatField(default = 0, blank = True, null = True)     
    PercentHPRegenMod = models.FloatField(default = 0, blank = True, null = True)    
    PercentLifeStealMod = models.FloatField(default = 0, blank = True, null = True)  
    PercentMPPoolMod = models.FloatField(default = 0, blank = True, null = True)     
    PercentMPRegenMod = models.FloatField(default = 0, blank = True, null = True)    
    PercentMagicDamageMod = models.FloatField(default = 0, blank = True, null = True)    
    PercentMovementSpeedMod = models.FloatField(default = 0, blank = True, null = True)  
    PercentPhysicalDamageMod = models.FloatField(default = 0, blank = True, null = True)     
    PercentSpellBlockMod = models.FloatField(default = 0, blank = True, null = True)     
    PercentSpellVampMod = models.FloatField(default = 0, blank = True, null = True)
    rFlatArmorModPerLevel = models.IntegerField(default = 0, blank = True, null = True)   
    rFlatArmorPenetrationMod = models.IntegerField(default = 0, blank = True, null = True)     
    rFlatArmorPenetrationModPerLevel = models.IntegerField(default = 0, blank = True, null = True)     
    rFlatCritChanceModPerLevel = models.FloatField(default = 0, blank = True, null = True)   
    rFlatCritDamageModPerLevel = models.IntegerField(default = 0, blank = True, null = True)   
    rFlatDodgeMod = models.IntegerField(default = 0, blank = True, null = True)    
    rFlatDodgeModPerLevel = models.IntegerField(default = 0, blank = True, null = True)    
    rFlatEnergyModPerLevel = models.IntegerField(default = 0, blank = True, null = True)   
    rFlatEnergyRegenModPerLevel = models.IntegerField(default = 0, blank = True, null = True)  
    rFlatGoldPer10Mod = models.IntegerField(default = 0, blank = True, null = True)    
    rFlatHPModPerLevel = models.IntegerField(default = 0, blank = True, null = True)   
    rFlatHPRegenModPerLevel = models.IntegerField(default = 0, blank = True, null = True)  
    rFlatMPModPerLevel = models.IntegerField(default = 0, blank = True, null = True)   
    rFlatMPRegenModPerLevel = models.IntegerField(default = 0, blank = True, null = True)  
    rFlatMagicDamageModPerLevel = models.IntegerField(default = 0, blank = True, null = True)  
    rFlatMagicPenetrationMod = models.IntegerField(default = 0, blank = True, null = True)    
    rFlatMagicPenetrationModPerLevel = models.IntegerField(default = 0, blank = True, null = True)     
    rFlatMovementSpeedModPerLevel = models.IntegerField(default = 0, blank = True, null = True)    
    rFlatPhysicalDamageModPerLevel = models.IntegerField(default = 0, blank = True, null = True)   
    rFlatSpellBlockModPerLevel = models.IntegerField(default = 0, blank = True, null = True)   
    rFlatTimeDeadMod = models.IntegerField(default = 0, blank = True, null = True)     
    rFlatTimeDeadModPerLevel = models.IntegerField(default = 0, blank = True, null = True)      
    rPercentArmorPenetrationMod = models.IntegerField(default = 0, blank = True, null = True)  
    rPercentArmorPenetrationModPerLevel = models.IntegerField(default = 0, blank = True, null = True)   
    rPercentAttackSpeedModPerLevel = models.IntegerField(default = 0, blank = True, null = True)    
    rPercentCooldownMod = models.IntegerField(default = 0, blank = True, null = True)  
    rPercentCooldownModPerLevel = models.IntegerField(default = 0, blank = True, null = True)  
    rPercentMagicPenetrationMod = models.IntegerField(default = 0, blank = True, null = True)  
    rPercentMagicPenetrationModPerLevel = models.IntegerField(default = 0, blank = True, null = True)  
    rPercentMovementSpeedModPerLevel = models.IntegerField(default = 0, blank = True, null = True)      
    rPercentTimeDeadMod = models.IntegerField(default = 0, blank = True, null = True)  
    rPercentTimeDeadModPerLevel = models.IntegerField(default = 0, blank = True, null = True)  

    def __unicode__(self):
        return unicode("Riot ID "+str(self.riot_id)+" "+self.name)

