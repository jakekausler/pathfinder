angular.module('pathfinder', ['ngMaterial','ngSanitize'])
	.config(function($mdThemingProvider) {
        $mdThemingProvider.theme('default')
            .primaryPalette('indigo')
            .accentPalette('pink')
            .warnPalette('red')
            .backgroundPalette('indigo')
    })
    .controller('pathfinderController', function($scope, $http, $mdToast, $mdMedia, $mdDialog) {
        $scope.display = 'main';
        $scope.chooseCharacter = function() {
        }
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
                    for (var i=0; i<10; i++) {
                        for (var j=0; j<cls.PreparedSpells[i].length; j++) {
                            $scope.characterSpells[cls.Type][i][j].Spell.UsesLeft = $scope.characterSpells[cls.Type][i][j].Uses
                            $scope.characterSpells[cls.Type][i][j] = $scope.characterSpells[cls.Type][i][j].Spell
                        }
                        if (cls.DomainSpells) {
                            $scope.characterSpells[cls.Type][i].push.apply($scope.characterSpells[cls.Type][i], cls.DomainSpells[i])
                            for (var j=$scope.characterSpells[cls.Type][i].length-cls.DomainSpells[i].length; j<$scope.characterSpells[cls.Type][i].length + cls.DomainSpells[i].length-1; j++) {
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
        }

        $scope.getNumberArray = function(n) {
            var arr = []
            for (i=0; i<n; i++) {
                arr.push(i)
            }
            return arr
        }

        $scope.isPortrait = function() {
            return $mdMedia('portrait');
        }

        $scope.showSkillDialog = function($event, skillIdx) {
            $mdDialog.show({
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

        $scope.showDamageDialog = function($event) {
            $mdDialog.show({
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

        $scope.showWeaponDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: WeaponController,
                templateUrl: 'main/items/weapons/weapondialog.html'
            });
        }

        function WeaponController($scope, $mdDialog, $mdToast, $http, parent) {
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

        $scope.showArmorDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: ArmorController,
                templateUrl: 'main/items/armor/armordialog.html'
            });
        }

        function ArmorController($scope, $mdDialog, $mdToast, $http, parent) {
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

        $scope.showShieldDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: ShieldController,
                templateUrl: 'main/items/armor/shielddialong.html'
            });
        }

        function ShieldController($scope, $mdDialog, $mdToast, $http, parent) {
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

        $scope.showMagicalProtectiveDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: MagicalProtectiveController,
                templateUrl: 'main/items/magical/magicaldialog.html'
            });
        }

        function MagicalProtectiveController($scope, $mdDialog, $mdToast, $http, parent) {
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

        $scope.showFeatDialog = function($event, idx) {
            $mdDialog.show({
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

        $scope.showClassDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: ClassController,
                templateUrl: 'main/'
            });
        }

        function ClassController($scope, $mdDialog, $mdToast, $http, parent) {
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

        $scope.showGoldDialog = function($event) {
            $mdDialog.show({
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

        $scope.showItemsDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: ItemsController,
                templateUrl: 'inventory/items/itemdialog.html'
            });
        }

        function ItemsController($scope, $mdDialog, $mdToast, $http, parent) {
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

        $scope.showSpellDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: SpellController,
                templateUrl: 'spell/spelldialog.html'
            });
        }

        function SpellController($scope, $mdDialog, $mdToast, $http, parent) {
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

        $scope.showPrepareSpellDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: PrepareSpellController,
                templateUrl: 'spell/preparespelldialog.html'
            });
        }

        function PrepareSpellController($scope, $mdDialog, $mdToast, $http, parent) {
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

        $scope.showKnowSpellDialog = function($event) {
            // TODO
            $mdDialog.show({
                targetEvent: $event,
                locals: {
                    parent: $scope
                },
                controller: KnowSpellController,
                templateUrl: 'spell/learnspelldialog.html'
            });
        }

        function KnowSpellController($scope, $mdDialog, $mdToast, $http, parent) {
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
    });