# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CellMaker
                                 A QGIS plugin
 Create and populate rectangular cells
                             -------------------
        begin                : 2013-12-12
        copyright            : (C) 2013 by Bo Victor Thomsen
        email                : bvt@aestas.dk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load CellMaker class from file CellMaker
    from cellmaker import CellMaker
    return CellMaker(iface)
