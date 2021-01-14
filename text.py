# text.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model astrolabe.
#
# Copyright (C) 2010-2020 Dominic Ford <dcf21-www@dcford.org.uk>
#
# This code is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# You should have received a copy of the GNU General Public License along with
# this file; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA

# ----------------------------------------------------------------------------

# A list of text strings, which we can render in various languages

text = {
    "en":
        {
            "months": [
                [31, "JANUÁR"],
                [28, "FEBRUÁR"],
                [31, "MÁRCIUS"],
                [30, "ÁPRILIS"],
                [31, "MÁJUS"],
                [30, "JÚNIUS"],
                [31, "JÚLIUS"],
                [31, "AUGUSZTUS"],
                [30, "SZEPTEMBER"],
                [31, "OKTÓBER"],
                [30, "NOVEMBER"],
                [31, "DECEMBER"]
            ],
            "zodiacal_constellations": [
                {"name": "Kos", "symbol": "\u2648"},
                {"name": "Bika", "symbol": "\u2649"},
                {"name": "Ikrek", "symbol": "\u264a"},
                {"name": "Rák", "symbol": "\u264b"},
                {"name": "Oroszlán", "symbol": "\u264c"},
                {"name": "Szűz", "symbol": "\u264d"},
                {"name": "Mérleg", "symbol": "\u264e"},
                {"name": "Skorpió", "symbol": "\u264f"},
                {"name": "Nyilas", "symbol": "\u2650"},
                {"name": "Bak", "symbol": "\u2651"},
                {"name": "Vízöntő", "symbol": "\u2652"},
                {"name": "Halak", "symbol": "\u2653"},
            ],
            "url": "https://in-the-sky.org/astrolabe/index.html",
            "copyright": "\u00A9 Dominic Ford 2020",
            "climate_latitude": "Tympanum a {:02d}{:s} szélességhez",
            "name": "Name",
            "directions": ["É", "ÉÉNy", "ÉNy", "NyÉNy", "Ny", "NyDNy", "DNy", "DDNy",
                           "D", "DDK", "DK", "KDK", "K", "KÉK", "ÉK", "ÉÉK"],
            "midnight": "Éjfél"
        },
    "fr":
        {
            "months": [
                [31, "JANVIER"],
                [28, "FÉVRIER"],
                [31, "MARS"],
                [30, "AVRIL"],
                [31, "MAI"],
                [30, "JUIN"],
                [31, "JUILLET"],
                [31, "AOÛT"],
                [30, "SEPTEMBRE"],
                [31, "OCTOBRE"],
                [30, "NOVEMBRE"],
                [31, "DÉCEMBRE"]
            ],
            "zodiacal_constellations": [
                {"name": "Bélier", "symbol": "\u2648"},
                {"name": "Taureau", "symbol": "\u2649"},
                {"name": "Gémeaux", "symbol": "\u264a"},
                {"name": "Cancer", "symbol": "\u264b"},
                {"name": "Lion", "symbol": "\u264c"},
                {"name": "Vierge", "symbol": "\u264d"},
                {"name": "Balance", "symbol": "\u264e"},
                {"name": "Scorpion", "symbol": "\u264f"},
                {"name": "Sagittaire", "symbol": "\u2650"},
                {"name": "Capricorne", "symbol": "\u2651"},
                {"name": "Verseau", "symbol": "\u2652"},
                {"name": "Poissons", "symbol": "\u2653"},
            ],
            "url": "https://in-the-sky.org/astrolabe/index.html",
            "copyright": "\u00A9 Dominic Ford 2020",
            "climate_latitude": "Climate prepared for latitude {:02d}\u00b0{:s}",
            "name": "Nom",
            "directions": ["N", "NNO", "NO", "ONO", "O", "OSO", "SO", "SSO",
                           "S", "SSE", "SE", "ESE", "E", "ENE", "NE", "NNE"],
            "midnight": "Minuit"
        },
    "sv":
        {
            "months": [
                [31, "JANUARI"],
                [28, "FÉBRUARI"],
                [31, "MARS"],
                [30, "APRIL"],
                [31, "MAJ"],
                [30, "JUNI"],
                [31, "JULI"],
                [31, "AUGUSTI"],
                [30, "SEPTEMBER"],
                [31, "OKTOBER"],
                [30, "NOVEMBER"],
                [31, "DECEMBER"]
            ],
            "zodiacal_constellations": [
                {"name": "Väduren", "symbol": "\u2648"},
                {"name": "Oxen", "symbol": "\u2649"},
                {"name": "Tvillingarna", "symbol": "\u264a"},
                {"name": "Kräftan", "symbol": "\u264b"},
                {"name": "Lejonet", "symbol": "\u264c"},
                {"name": "Jungfrun", "symbol": "\u264d"},
                {"name": "Vågen", "symbol": "\u264e"},
                {"name": "Skorpionen", "symbol": "\u264f"},
                {"name": "Skytten", "symbol": "\u2650"},
                {"name": "Stenbocken", "symbol": "\u2651"},
                {"name": "Vattumannen", "symbol": "\u2652"},
                {"name": "Fiskarna", "symbol": "\u2653"},
            ],
            "url": "https://in-the-sky.org/astrolabe/index.html",
            "copyright": "\u00A9 Dominic Ford 2020",
            "climate_latitude": "Climate prepared for latitude {:02d}\u00b0{:s}",
            "name": "Namn",
            "directions": ["N", "NNV", "NV", "VNV", "V", "VSV", "SV", "SSV",
                           "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"],
            "midnight": "Midnight"
        }
}
