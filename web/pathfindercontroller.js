angular.module('pathfinder', ['ngMaterial', 'ngSanitize'])
    .config(function($mdThemingProvider) {
        $mdThemingProvider.theme('default')
            .primaryPalette('indigo')
            .accentPalette('pink')
            .warnPalette('red')
            .backgroundPalette('indigo')
    })
    .controller('pathfinderController', function($scope, $http, $mdToast, $mdMedia, $mdDialog) {
        $scope.display = 'main';
        $scope.chooseCharacter = function() {}
        $scope.main = function() {
            $scope.display = 'main';
        }
        $scope.inventory = function() {
            $scope.display = 'inventory';
        }
        $scope.spells = function() {
            $scope.display = 'spells';
        }
        $scope.simulator = function() {
            $scope.display = 'simulator';
        }

        $scope.character = null;
        $scope.updateCharacter = function() {
            $http({
                url: 'character',
                method: 'GET',
                params: {
                    id: 'uuid'
                }
            }).then(function(response) {
                $scope.character = response.data;
                $scope.updateSpells();
            }, function(response) {
                $mdToast.showSimple("Failed to get character: " + response.data);
            });
        };
        $scope.updateCharacter();

        $scope.IncreaseSkill = function(skillid, value) {
            $http({
                url: 'character/skill/rank',
                method: 'POST',
                params: {
                    id: $scope.character.Id,
                    skillid: skillid,
                    value: value
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }, function(response) {
                $mdToast.showSimple("Failed: " + response.data);
            });
        }

        $scope.characterSpells = {}
        $scope.updateSpells = function() {
            $scope.characterSpells = {}
            for (c in $scope.character.Classes) {
                var cls = $scope.character.Classes[c].Class
                $scope.characterSpells[cls.Type] = []
                if (cls.MustPrepare) {
                    $scope.characterSpells[cls.Type] = cls.PreparedSpells;
                    for (var i = 0; i < 10; i++) {
                        for (var j = 0; j < cls.PreparedSpells[i].length; j++) {
                            $scope.characterSpells[cls.Type][i][j].Spell.UsesLeft = $scope.characterSpells[cls.Type][i][j].Uses
                            $scope.characterSpells[cls.Type][i][j] = $scope.characterSpells[cls.Type][i][j].Spell
                        }
                        if (cls.DomainSpells) {
                            $scope.characterSpells[cls.Type][i].push.apply($scope.characterSpells[cls.Type][i], cls.DomainSpells[i])
                            for (var j = $scope.characterSpells[cls.Type][i].length - cls.DomainSpells[i].length; j < $scope.characterSpells[cls.Type][i].length; j++) {
                                $scope.characterSpells[cls.Type][i][j].Spell.IsDomain = true
                                $scope.characterSpells[cls.Type][i][j].Spell.UsesLeft = $scope.characterSpells[cls.Type][i][j].Uses
                                $scope.characterSpells[cls.Type][i][j] = $scope.characterSpells[cls.Type][i][j].Spell
                            }
                        }
                    }
                } else {
                    $scope.characterSpells[cls.Type] = cls.KnownSpells
                }
            }
        }

        $scope.getSpellDescriptors = function(spell) {
            ret = ""
            if (spell.School) {
                ret += spell.School
            }
            if (spell.Subschools.length > 0) {
                ret += " (" + spell.Subschools.join(",") + ")"
            }
            if (spell.Descriptors.length > 0) {
                ret += " [" + spell.Descriptors.join(",") + "]"
            }
            return ret
        }

        $scope.getComponents = function(spell, UseDivineComponent) {
            ret = ""
            if (spell.VerbalComponent) {
                if (ret != "") {
                    ret += ", "
                }
                ret += "V"
            }
            if (spell.SomaticComponent) {
                if (ret != "") {
                    ret += ", "
                }
                ret += "S"
            }
            if (spell.DivineFocusComponent.DivineFocusComponent[0] && UseDivineComponent) {
                if (ret != "") {
                    ret += ", "
                }
                ret += "DF"
            } else {
                materials = []
                if (spell.MaterialComponent.MaterialComponent[0]) {
                    if (ret != "") {
                        ret += ", "
                    }
                    ret += "M"
                    materials = spell.MaterialComponent.MaterialComponent[1]
                }
                if (spell.FocusComponent.FocusComponent[0]) {
                    if (ret != "") {
                        ret += ", "
                    }
                    ret += "F"
                    materials = spell.FocusComponent.FocusComponent[1]
                }
                if (materials.length > 0) {
                    ret += " (" + materials.join("; ") + ")"
                }
            }
            return ret
        }

        $scope.getNumberArray = function(n) {
            var arr = []
            for (i = 0; i < n; i++) {
                arr.push(i)
            }
            return arr
        }

        $scope.isPortrait = function() {
            return $mdMedia('portrait');
        }

        $scope.showSkillDialog = function($event, skillIdx) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    skill: $scope.character.Skills[skillIdx],
                    parent: $scope
                },
                controller: SkillDialogController,
                templateUrl: 'main/skills/skillchangedialog.html'
            });
        }

        function SkillDialogController($scope, $mdDialog, $mdToast, $http, skill, parent) {
            $scope.parent = parent;
            $scope.skill = skill;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function() {
                $http({
                    url: 'character/skill/rank',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        skillid: $scope.skill.SkillId,
                        value: $scope.skill.Ranks
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    $scope.parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            }
        }

        $scope.showFCSkillDialog = function($event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: FCSkillDialogController,
                templateUrl: 'main/skills/applyfcpointsdialog.html'
            });
        }

        function FCSkillDialogController($scope, $mdDialog, $mdToast, $http, parent) {
            $scope.parent = parent;
            $scope.skill = -1;
            $scope.amount = 0;
            $scope.skills = null;
            $scope.loadSkills = function() {
                return $http({
                    url: 'skills',
                    method: 'GET'
                }).then(function(response) {
                    $scope.skills = response.data;
                });
            };
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function() {
                $http({
                    url: 'character/skill/applyfcpoints',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        skillid: $scope.skill,
                        value: $scope.amount
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    $scope.parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            }
        }

        $scope.showDamageDialog = function($event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: DamageController,
                templateUrl: 'main/health/damagedialog.html'
            });
        }

        function DamageController($scope, $mdDialog, $mdToast, $http, parent) {
            $scope.parent = parent;
            $scope.amount = 0;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/health/' + type,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        amount: $scope.amount
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showAbilityDialog = function($event, key) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    key: key
                },
                controller: AbilityController,
                templateUrl: 'main/abilities/abilitydialog.html'
            });
        }

        function AbilityController($scope, $mdDialog, $mdToast, $http, parent, key) {
            $scope.parent = parent;
            $scope.key = key;
            $scope.amount = 0;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/ability/' + type,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        ability: $scope.key,
                        amount: $scope.amount
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showLanguageDialog = function($event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: LanguageController,
                templateUrl: 'main/languages/languagedialog.html'
            });
        }

        function LanguageController($scope, $mdDialog, $mdToast, $http, parent) {
            $scope.parent = parent;
            $scope.newLanguage = '';
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type, language) {
                $http({
                    url: 'character/language/' + type,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        value: language
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showFeatDialog = function($event, idx) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    idx: idx
                },
                controller: FeatController,
                templateUrl: 'main/feats/featdialog.html'
            });
        }

        function FeatController($scope, $mdDialog, $mdToast, $http, parent, idx) {
            $scope.parent = parent;
            $scope.idx = idx;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function() {
                $http({
                    url: 'character/feat/forget',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        value: $scope.idx
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showAddFeatDialog = function($event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: AddFeatController,
                templateUrl: 'main/feats/addfeatdialog.html'
            });
        }

        function AddFeatController($scope, $mdDialog, $mdToast, $http, parent) {
            $scope.parent = parent;
            $scope.selectedItem = null;
            $scope.searchText = null;
            $scope.querySearch = function(query) {
                return $scope.loadFeats(query);
            }
            $scope.loadFeats = function(query) {
                return $http({
                    url: 'feats',
                    method: 'GET',
                    params: {
                        id: $scope.parent.character.Id,
                        searchtext: query
                    }
                }).then(function(response) {
                    return response.data;
                });
            }
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function() {
                $http({
                    url: 'character/feat/learn',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        value: $scope.selectedItem.ID
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showAddClassDialog = function($event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: AddClassController,
                templateUrl: 'main/classes/newclassdialog.html'
            });
        }

        function AddClassController($scope, $mdDialog, $mdToast, $http, parent) {
            $scope.parent = parent;
            $scope.classId = -1;
            $scope.classes;
            $scope.loadClasses = function() {
                return $http({
                    url: 'classes',
                    method: 'GET',
                    params: {
                        id: $scope.parent.character.Id
                    }
                }).then(function(response) {
                    $scope.classes = response.data;
                });
            };
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function() {
                $http({
                    url: 'character/class/add',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        classidx: $scope.classId
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showClassDialog = function($event, className, classIdx) {
            console.log(className)
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    className: className,
                    classIdx: classIdx
                },
                controller: ClassController,
                templateUrl: 'main/classes/classdialog.html'
            });
        }

        function ClassController($scope, $mdDialog, $mdToast, $http, parent, className, classIdx) {
            $scope.parent = parent;
            $scope.className = className;
            $scope.classIdx = classIdx;
            $scope.amount = 0;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/class/' + type,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        value: $scope.amount,
                        classidx: $scope.classIdx
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showGoldDialog = function($event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: GoldController,
                templateUrl: 'inventory/golddialog.html'
            });
        }

        function GoldController($scope, $mdDialog, $mdToast, $http, parent) {
            $scope.parent = parent;
            $scope.amount = 0;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/gold/' + type,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        value: $scope.amount
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showExperienceDialog = function($event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: ExperienceController,
                templateUrl: 'inventory/experiencedialog.html'
            });
        }

        function ExperienceController($scope, $mdDialog, $mdToast, $http, parent) {
            $scope.parent = parent;
            $scope.amount = 0;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/experience/' + type,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        value: $scope.amount
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showEquipmentDialog = function($event) {
            // TODO
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: EquipmentController,
                templateUrl: 'inventory/equipment/equipmentdialog.html'
            });
        }

        function EquipmentController($scope, $mdDialog, $mdToast, $http, parent) {
            // TODO
            $scope.parent = parent;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/' + type,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showItemsDialog = function($event, item, idx) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    item: item,
                    idx: idx
                },
                controller: ItemsController,
                templateUrl: 'inventory/items/itemdialog.html'
            });
        }

        function ItemsController($scope, $mdDialog, $mdToast, $http, parent, item, idx) {
            $scope.parent = parent;
            $scope.name = item.Item.Name;
            $scope.quantity = item.Quantity;
            $scope.value = item.Item.Value;
            $scope.weight = item.Item.Weight;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function() {
                $http({
                    url: 'character/item/edit',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        itemindex: idx,
                        name: $scope.name,
                        quantity: $scope.quantity,
                        value: $scope.value,
                        weight: $scope.weight
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
            $scope.remove = function() {
                $http({
                    url: 'character/item/remove',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        itemindex: idx
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showNewItemDialog = function($event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: NewItemController,
                templateUrl: 'inventory/items/newitemdialog.html'
            });
        }

        function NewItemController($scope, $mdDialog, $mdToast, $http, parent) {
            $scope.parent = parent;

            $scope.itemType = "";
            $scope.name = ""
            $scope.quantity = 0
            $scope.value = 0;
            $scope.weight = 0;

            $scope.weaponType = "";
            $scope.damage = "";
            $scope.critical = "";
            $scope.range = 0;
            $scope.weaponAttackTypes = [];
            $scope.usesAllTypes = false;
            $scope.weaponSpecials = [];
            $scope.usesAllSpecials = false;
            $scope.twoHanded = false;
            $scope.light = false;
            $scope.martial = false;
            $scope.exotic = false;
            $scope.masterwork = false;
            $scope.enchantment = 0;
            $scope.size = "";

            $scope.wearableType = "";
            $scope.applicableSlots = [];
            $scope.cancelsSlots = [];
            $scope.weightType = "";
            $scope.armorClass = 0;
            $scope.armorCheckPenalty = 0;
            $scope.maxDexBonus = 0;

            $scope.ammoType = "";
            $scope.extraDamage = "";
            $scope.extraRange = 0;
            $scope.extraAttack = 0;

            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function() {
                url = 'character/item/add/' + $scope.itemType.toLowerCase();
                if ($scope.itemType == 'Weapon') {
                    url += '/' + $scope.weaponType.toLowerCase();
                } else if ($scope.itemType == 'Wearable') {
                    url += '/' + $scope.wearableType.toLowerCase().replace(' ', '');
                }
                $http({
                    url: url,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        itemType: $scope.itemType,
                        name: $scope.name,
                        quantity: $scope.quantity,
                        value: $scope.value,
                        weight: $scope.weight,
                        weapontype: $scope.weaponType,
                        damage: $scope.damage,
                        critical: $scope.critical,
                        range: $scope.range,
                        weaponattacktypes: $scope.weaponAttackTypes,
                        usesalltypes: $scope.usesAllTypes,
                        weaponSpecials: $scope.weaponSpecials,
                        usesallspecials: $scope.usesAllSpecials,
                        twohanded: $scope.twoHanded,
                        light: $scope.light,
                        martial: $scope.martial,
                        exotic: $scope.exotic,
                        masterwork: $scope.masterwork,
                        enchantment: $scope.enchantment,
                        size: $scope.size,
                        wearabletype: $scope.wearableType,
                        weighttype: $scope.weightType,
                        applicableslots: $scope.applicableSlots,
                        cancelsslots: $scope.cancelsSlots,
                        ammotype: $scope.ammoType,
                        extradamage: $scope.extraDamage,
                        extrarange: $scope.extraRange,
                        extraattack: $scope.extraAttack
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
            $scope.itemTypes = ['Item', 'Weapon', 'Wearable', 'Ammunition']

            $scope.weaponTypes = ['Unarmed', 'Melee', 'Ranged']
            $scope.attackTypes = ["Bludgeoning", "Slashing", "Peircing"]
            $scope.specials = ["Blocking", "Brace", "Deadly", "Disarm", "Distracting", "Double", "Fragile", "Grapple", "Monk", "Nonlethal", "Performance", "Reach", "Strength", "Sunder", "Trip"]
            $scope.sizes = ["Fine", "Diminutive", "Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan", "Colossal"];

            $scope.wearableTypes = ['Shield', 'Armor', 'Magical Protection', 'Other']
            $scope.weightTypes = ["Light", "Medium", "Heavy"];

            $scope.ammoTypes = ['Arrow', 'Dart', 'Bolt', 'Sling Bullet', 'Shuriken']
        }

        $scope.unequip = function($event, item) {
            $http({
                    url: 'character/equipment/unequip',
                    method: 'POST',
                    params: {
                        id: $scope.character.Id,
                        slot: item.EquippedAtSlot[0]
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    $scope.updateCharacter();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
        }

        $scope.showEquipDialog = function($event, item, itemIdx) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    item: item,
                    itemIdx: itemIdx
                },
                controller: EquipController,
                templateUrl: 'inventory/items/equipdialog.html'
            });
        }

        function EquipController($scope, $mdDialog, $mdToast, $http, parent, item, itemIdx) {
            $scope.parent = parent;
            $scope.item = item;
            $scope.itemIdx = itemIdx;
            $scope.slot = 0;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/equipment/equip',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        itemid: $scope.itemIdx,
                        slot: $scope.slot
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showEquipmentEquipDialog = function($event, slot) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    slot: slot
                },
                controller: EquipmentEquipController,
                templateUrl: 'inventory/equipment/equipmentdialog.html'
            });
        }

        function EquipmentEquipController($scope, $mdDialog, $mdToast, $http, parent, slot) {
            $scope.parent = parent;
            $scope.slot = slot;
            $scope.itemid = -1;
            $scope.items = [];
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/equipment/equip',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        itemid: $scope.itemid,
                        slot: $scope.slot
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
            $scope.loadEquipableItems = function() {
                return $http({
                    url: 'equipableitems',
                    method: 'GET',
                    params: {
                        id: $scope.parent.character.Id,
                        slot: $scope.slot
                    }
                }).then(function(response) {
                    $scope.items = response.data;
                });
            };
        }

        $scope.showSpellDialog = function($event, classIndex, level, idx, mustPrepare, domain, description) {
            if (domain) {
                idx = 0;
            }
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    classIndex: classIndex,
                    level: level,
                    idx: idx,
                    mustPrepare: mustPrepare,
                    domain: domain,
                    description: description
                },
                controller: PrepareUseSpellController,
                templateUrl: 'spell/spelldialog.html'
            });
        }

        function PrepareUseSpellController($scope, $mdDialog, $mdToast, $http, parent, classIndex, level, idx, mustPrepare, domain, description) {
            $scope.parent = parent;
            $scope.classIndex = classIndex;
            $scope.level = level;
            $scope.idx = idx;
            $scope.mustPrepare = mustPrepare;
            $scope.domain = domain == true;
            $scope.amount = 0
            $scope.description = description;
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/spell/' + type,
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        classindex: $scope.classIndex,
                        level: $scope.level,
                        spellidx: $scope.idx,
                        domain: $scope.domain,
                        value: $scope.amount
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showPrepareSpellDialog = function($event, classindex, level, hasDomains) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    level: level,
                    classindex: classindex,
                    hasDomains: hasDomains
                },
                controller: PrepareSpellController,
                templateUrl: 'spell/preparespelldialog.html'
            });
        }

        function PrepareSpellController($scope, $mdDialog, $mdToast, $http, parent, level, classindex, hasDomains) {
            $scope.parent = parent;
            $scope.level = level;
            $scope.classindex = classindex;
            $scope.domain = false;
            $scope.hasDomains = hasDomains;
            $scope.selectedItem = null;
            $scope.searchText = null;
            $scope.changeDomain = function() {
                $scope.searchText = null;
                $scope.selectedItem = null;
            }
            $scope.querySearch = function(query) {
                return $scope.loadSpells(query);
            }
            $scope.loadSpells = function(query) {
                return $http({
                    url: 'spells',
                    method: 'GET',
                    params: {
                        id: $scope.parent.character.Id,
                        classidx: $scope.classindex,
                        level: $scope.level,
                        domain: $scope.domain ? 'true' : 'false',
                        searchtext: query
                    }
                }).then(function(response) {
                    return response.data;
                });
            }
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/spell/prepare',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        classindex: $scope.classindex,
                        domain: $scope.domain,
                        value: $scope.selectedItem.Id
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.showLearnSpellDialog = function($event, classindex, level, hasDomains) {
            $mdDialog.show({
                clickOutsideToClose: true,
                targetEvent: $event,
                locals: {
                    parent: $scope,
                    level: level,
                    classindex: classindex,
                    hasDomains: hasDomains
                },
                controller: LearnSpellController,
                templateUrl: 'spell/learnspelldialog.html'
            });
        }

        function LearnSpellController($scope, $mdDialog, $mdToast, $http, parent, level, classindex, hasDomains) {
            $scope.parent = parent;
            $scope.level = level;
            $scope.classindex = classindex;
            $scope.domain = false;
            $scope.hasDomains = hasDomains;
            $scope.selectedItem = null;
            $scope.searchText = null;
            $scope.changeDomain = function() {
                $scope.searchText = null;
                $scope.selectedItem = null;
            }
            $scope.querySearch = function(query) {
                return $scope.loadSpells(query);
            }
            $scope.loadSpells = function(query) {
                return $http({
                    url: 'spells',
                    method: 'GET',
                    params: {
                        id: $scope.parent.character.Id,
                        classidx: $scope.classindex,
                        level: $scope.level,
                        domain: $scope.domain ? 'true' : 'false',
                        searchtext: query
                    }
                }).then(function(response) {
                    return response.data;
                });
            }
            $scope.cancel = function() {
                $mdDialog.hide();
            };
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.save = function(type) {
                $http({
                    url: 'character/spell/learn',
                    method: 'POST',
                    params: {
                        id: $scope.parent.character.Id,
                        classindex: $scope.classindex,
                        domain: $scope.domain,
                        value: $scope.selectedItem.Id
                    }
                }).then(function(response) {
                    $mdToast.showSimple("Success: " + response.data);
                    parent.updateCharacter();
                    $scope.hide();
                }, function(response) {
                    $mdToast.showSimple("Failed: " + response.data);
                });
            };
        }

        $scope.resetAllClasses = function() {
            $http({
                url: 'character/spell/resetall',
                method: 'POST',
                params: {
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }, function(response) {
                $mdToast.showSimple("Failed: " + response.data);
            });
        }

        $scope.resetClass = function(classIdx) {
            $http({
                url: 'character/spell/resetclass',
                method: 'POST',
                params: {
                    id: $scope.character.Id,
                    classindex: classIdx
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }, function(response) {
                $mdToast.showSimple("Failed: " + response.data);
            });
        }

        $scope.resetLevel = function(classIdx, level) {
            $http({
                url: 'character/spell/resetlevel',
                method: 'POST',
                params: {
                    id: $scope.character.Id,
                    classindex: classIdx,
                    level: level
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }, function(response) {
                $mdToast.showSimple("Failed: " + response.data);
            });
        }


        $scope.updateName = function() {
            $http({
                url: 'character/information/name/change',
                method: 'POST',
                params: {
                    value: $scope.character.Name,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updatePlayer = function() {
            $http({
                url: 'character/information/player/change',
                method: 'POST',
                params: {
                    value: $scope.character.PlayerName,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateAlignment = function() {
            $http({
                url: 'character/information/alignment/change',
                method: 'POST',
                params: {
                    value: $scope.character.Alignment,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateRace = function() {
            $http({
                url: 'character/information/race/change',
                method: 'POST',
                params: {
                    value: $scope.character.Race,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateDiety = function() {
            $http({
                url: 'character/information/diety/change',
                method: 'POST',
                params: {
                    value: $scope.character.Diety,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateSize = function() {
            $http({
                url: 'character/information/size/change',
                method: 'POST',
                params: {
                    value: $scope.character.Size,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateGender = function() {
            $http({
                url: 'character/information/gender/change',
                method: 'POST',
                params: {
                    value: $scope.character.Gender,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateAge = function() {
            $http({
                url: 'character/information/age/change',
                method: 'POST',
                params: {
                    value: $scope.character.Age,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateHeight = function() {
            $http({
                url: 'character/information/height/change',
                method: 'POST',
                params: {
                    value: $scope.character.Height,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateWeight = function() {
            $http({
                url: 'character/information/weight/change',
                method: 'POST',
                params: {
                    value: $scope.character.Weight,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateHair = function() {
            $http({
                url: 'character/information/hair/change',
                method: 'POST',
                params: {
                    value: $scope.character.HairColor.Name,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateEye = function() {
            $http({
                url: 'character/information/eye/change',
                method: 'POST',
                params: {
                    value: $scope.character.EyeColor.Name,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }
        $scope.updateHomeland = function() {
            $http({
                url: 'character/information/homeland/change',
                method: 'POST',
                params: {
                    value: $scope.character.Homeland,
                    id: $scope.character.Id
                }
            }).then(function(response) {
                $mdToast.showSimple("Success: " + response.data);
                $scope.updateCharacter();
            }).then(function(response) {
                $mdToast("Failure: " + response.data);
            });
        }

        $scope.alignments = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "Neutral Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
        $scope.races = [];
        $scope.sizes = ["Fine", "Diminutive", "Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan", "Colossal"];
        $scope.classes = [];
        $scope.colors = [];
        $scope.genders = ["Male", "Female", "Genderless", "Both"];
        $scope.updateRaces = function() {
            $http({
                url: 'races',
                method: 'GET'
            }).then(function(response) {
                $scope.races = response.data;
            }, function(response) {
                $mdToast.showSimple("Failed to get races: " + response.data);
            });
        }
        $scope.updateRaces();
        $scope.updateClasses = function() {
            $http({
                url: 'classes',
                method: 'GET'
            }).then(function(response) {
                $scope.classes = response.data;
            }, function(response) {
                $mdToast.showSimple("Failed to get classes: " + response.data);
            });
        }
        $scope.updateClasses();
        $scope.updateColors = function() {
            $http({
                url: 'colors',
                method: 'GET'
            }).then(function(response) {
                $scope.colors = response.data;
            }, function(response) {
                $mdToast.showSimple("Failed to get colors: " + response.data);
            });
        }
        $scope.updateColors();
    })
    .directive('dice', function() {
        return {
            require: 'ngModel',
            link: function(scope, elm, attrs, ctrl) {
                ctrl.$validators.integer = function(modelValue, viewValue) {
                    if (ctrl.$isEmpty(modelValue)) {
                        return true;
                    }
                    expression = /^[0-9]+d[0-9]+( ?\+ ?[0-9]+)?$/
                    if (expression.test(viewValue)) {
                        return true;
                    }
                    return false;
                }
            }
        };
    })
    .directive('crit', function() {
        return {
            require: 'ngModel',
            link: function(scope, elm, attrs, ctrl) {
                ctrl.$validators.integer = function(modelValue, viewValue) {
                    if (ctrl.$isEmpty(modelValue)) {
                        return true;
                    }
                    expression = /^([0-9]+(-[0-9]+)?\/)?x[0-9]+?$/
                    if (expression.test(viewValue)) {
                        return true;
                    }
                    return false;
                }
            }
        };
    });