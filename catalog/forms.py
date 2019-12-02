from django import forms


# Depreciated for aggregated into html file.
class PropertyList(forms.Form):
    apt_type_choice = [('all', 'Type'),
                       ('Townhouse', 'Townhouse'),
                       ('Miscellaneous', 'Miscellaneous'),
                       ('SingleFamily', 'Single Family'),
                       ('MultiFamily2To4', 'MultiFamily 2 To 4'),
                       ('MultiFamily5Plus', 'MultiFamily 5 Plus'),
                       ('Condominium', 'Condominium'),
                       ('Apartment', 'Apartment'),
                       ]
    apt_bedroom_choice = [('all', 'Type'),
                          ("1", "1"),
                          ("2", "2"),
                          ("3", "3"),
                          ("4", "4"),
                          ("5", "5"),
                          ]
    apt_bathroom_choice = [('all', 'Type'),
                           ("1", "1"),
                           ("2", "2"),
                           ("3", "3"),
                           ("4", "4"),
                           ("5", "5"),
                           ]
    apt_price_choice = [('all', "Price"),
                        ('500', "< $500"),
                        ('500-1000', '$500~$1,000'),
                        ('1000-1500', '$1,000~$1,500'),
                        ("1500-2000", '$1,500~$2,000'),
                        ("2000-2500", '$2,000~$2,500'),
                        ("2500-3000", '$2,500~$3,000'),
                        ('3000', '> 3000'),
                        ]

    apt_location = forms.CharField(label='apt-location', max_length=100)
    apt_type = forms.ChoiceField(label='option-apt-type', choices=apt_type_choice)
    apt_bedroom = forms.ChoiceField(label='option-apt-bedroom', choices=apt_bedroom_choice)
    apt_bathroom = forms.ChoiceField(label='option-apt-bathroom', choices=apt_bathroom_choice)
    apt_price = forms.ChoiceField(label='option-apt-price', choices=apt_price_choice)