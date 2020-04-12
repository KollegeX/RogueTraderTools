# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import os
import wx
import wx.xrc
import random
from wx.lib.intctrl import IntCtrl
from operator import itemgetter
import sqlite3

wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"

cwd = os.path.abspath(os.curdir)
conn = sqlite3.connect('colonies.db')
c = conn.cursor()

#Create table once
"""
c.execute('''CREATE TABLE colonies (name UNIQUE, type, contracted integer, profit integer, size integer, complacency integer, order integer, productivity integer, piety integer, fraction integer, year integer, millenium integer, governour, personality, minerals, addresources, organics, special, mineralsvalue integer, addresourcesvalue integer, organicsvalue integer, specialvalue integer, history)''')

"""

###########################################################################
## Class RT_Tools
###########################################################################


class RT_Tools(wx.Frame):
    def __init__(self, parent):
        """wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title="Navigation App",
            pos=wx.DefaultPosition,
            size=wx.Size(460, 750),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )"""
        super(RT_Tools, self).__init__(parent, size = (500,720))
        self.InitUI()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        #create menu (currently not used)
        '''
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu = wx.Menu()
        self.m_new_nav = wx.MenuItem(
            self.m_menu, wx.ID_NEW, u"New Navigation", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_menu.Append(self.m_new_nav)

        self.m_menu.AppendSeparator()

        self.m_save = wx.MenuItem(
            self.m_menu, wx.ID_SAVE, u"Save Ship", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_menu.Append(self.m_save)

        self.m_load = wx.MenuItem(
            self.m_menu, wx.ID_OPEN, u"Load Ship", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_menu.Append(self.m_load)

        self.m_menu.AppendSeparator()

        self.m_exit = wx.MenuItem(
            self.m_menu, wx.ID_EXIT, u"Exit", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_menu.Append(self.m_exit)

        self.m_menubar1.Append(self.m_menu, u"Menu")

        self.SetMenuBar(self.m_menubar1)

        self.Bind(wx.EVT_MENU, self.onNew, id=self.m_new_nav.GetId())
        self.Bind(wx.EVT_MENU, self.onSave, id=self.m_save.GetId())
        self.Bind(wx.EVT_MENU, self.onLoad, id=self.m_load.GetId())
        self.Bind(wx.EVT_MENU, self.onExit, id=self.m_exit.GetId())
        '''

    def InitUI(self):    
        nb = wx.Notebook(self) 
        nb.AddPage(Colonies(nb),"Colonies") 
        nb.AddPage(Navigation(nb),"Navigation") 
        self.Centre() 
        self.Show(True) 

    # Menu Factions
    def onNew(self, e):
        global restart
        restart = False
        win = RT_Tools(None)
        win.Show(True)
        self.SetTopWindow(win)
        return True

    def onSave(self, e):
        pass

    def onLoad(self, e):
        pass
 
    def onExit(self, e):
        self.Close(True)


class Colonies(wx.Panel): 
    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_name = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_name.Wrap( -1 )

        gbSizer1.Add( self.m_name, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.v_name = wx.TextCtrl( self, wx.ID_ANY, u"New Colony", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        self.v_name.SetName("Name")

        self.btn_save = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.btn_save, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn_load = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.btn_load, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_type = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_type.Wrap( -1 )

        gbSizer1.Add( self.m_type, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        ch_typesChoices = [ u"Agricultural", u"Industrial", u"Research", u"Ecclesiastical" ]
        self.ch_types = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, ch_typesChoices, 0 )
        gbSizer1.Add( self.ch_types, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_funded = wx.CheckBox( self, wx.ID_ANY, u"By Contract", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_funded, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.btn_generate = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.btn_generate, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_size = wx.StaticText( self, wx.ID_ANY, u"Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_size.Wrap( -1 )

        gbSizer1.Add( self.m_size, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.v_size = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_size, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_profit = wx.StaticText( self, wx.ID_ANY, u"Profit Factor", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_profit.Wrap( -1 )

        gbSizer1.Add( self.m_profit, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_comp = wx.StaticText( self, wx.ID_ANY, u"Complacency", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_comp.Wrap( -1 )

        gbSizer1.Add( self.m_comp, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_order = wx.StaticText( self, wx.ID_ANY, u"Order", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_order.Wrap( -1 )

        gbSizer1.Add( self.m_order, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_prod = wx.StaticText( self, wx.ID_ANY, u"Productivity", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_prod.Wrap( -1 )

        gbSizer1.Add( self.m_prod, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_piety = wx.StaticText( self, wx.ID_ANY, u"Piety", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_piety.Wrap( -1 )

        gbSizer1.Add( self.m_piety, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.v_profit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_profit, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.v_comp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_comp, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_order = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_order, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_prod = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_prod, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_piety = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_piety, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_frac = wx.StaticText( self, wx.ID_ANY, u"Fraction", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_frac.Wrap( -1 )

        gbSizer1.Add( self.m_frac, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_year = wx.StaticText( self, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_year.Wrap( -1 )

        gbSizer1.Add( self.m_year, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_mill = wx.StaticText( self, wx.ID_ANY, u"Millenium", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_mill.Wrap( -1 )

        gbSizer1.Add( self.m_mill, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.v_frac = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_frac, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_year = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_year, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_mill = wx.TextCtrl( self, wx.ID_ANY, u"41", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_mill, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.btn_calc = wx.Button( self, wx.ID_ANY, u"Calculate", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.btn_calc, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        self.m_gov = wx.TextCtrl( self, wx.ID_ANY, u"Governour", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_gov, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        ch_personalityChoices = [u"Beloved", u"Militarist", u"Corrupt", u"Idle", u"Ambitious", u"Zealous", u"Patron", u"Unlucky", u"Administrator", u"Cruel", u"Spymaster", u"Generalissimo", u"Paranoid", u"Mad", u"Charitable", u"Vainglorious", u"Scholarly", u"Avaricious"]
        self.ch_personality = wx.ComboBox( self, wx.ID_ANY, u"Personality", wx.DefaultPosition, wx.DefaultSize, ch_personalityChoices, 0 )
        gbSizer1.Add( self.ch_personality, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        ch_representativeChoices = [u"Satrap", u"Judge", u"Cardinal", u"Colonist", u"General", u"Dynasty Member"]
        self.ch_representative = wx.ComboBox( self, wx.ID_ANY, u"Representative", wx.DefaultPosition, wx.DefaultSize, ch_representativeChoices, 0 )
        gbSizer1.Add( self.ch_representative, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.btn_status = wx.Button( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.btn_status, wx.GBPosition( 7, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

        m_supp_upgradesChoices = [u"Arbites Precinct", u"Eccl. Mission", u"Mechanicum Station", u"Infantry Garrison", u"Navy Station", u"Cultural Monument", u"Industrial Facility", u"Personal Lodgings", u"Contacts", u"Trappings"]
        self.m_supp_upgrades = wx.ComboBox( self, wx.ID_ANY, u"Infrastructure", wx.DefaultPosition, wx.DefaultSize, m_supp_upgradesChoices, 0 )
        gbSizer1.Add( self.m_supp_upgrades, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_main_upgradesChoices = [u"Transport", u"Power", u"Water", u"Food & Distro", u"Communication" ]
        self.m_main_upgrades = wx.ComboBox( self, wx.ID_ANY, u"Support", wx.DefaultPosition, wx.DefaultSize, m_main_upgradesChoices, 0 )
        gbSizer1.Add( self.m_main_upgrades, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_upgrade_time = wx.TextCtrl( self, wx.ID_ANY, u"Time (fractions)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_upgrade_time, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn_upgrade = wx.Button( self, wx.ID_ANY, u"Apply Upgrade", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.btn_upgrade, wx.GBPosition( 8, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_resource1 = wx.StaticText( self, wx.ID_ANY, u"Minerals", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_resource1.Wrap( -1 )

        gbSizer1.Add( self.m_resource1, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_resource2 = wx.StaticText( self, wx.ID_ANY, u"Add.Resource", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_resource2.Wrap( -1 )

        gbSizer1.Add( self.m_resource2, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_resource3 = wx.StaticText( self, wx.ID_ANY, u"Organics", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_resource3.Wrap( -1 )

        gbSizer1.Add( self.m_resource3, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_resource4 = wx.StaticText( self, wx.ID_ANY, u"Special", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_resource4.Wrap( -1 )

        gbSizer1.Add( self.m_resource4, wx.GBPosition( 9, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        ch_resource1Choices = [u"Industrial", u"Ornamental", u"Radioactive", u"Exotic Material"]
        self.ch_resource1 = wx.ComboBox( self, wx.ID_ANY, u"Minerals", wx.DefaultPosition, wx.DefaultSize, ch_resource1Choices, 0 )
        gbSizer1.Add( self.ch_resource1, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        ch_resource2Choices = [u"Archeotech Cache", u"Minerals", u"Organic Compound", u"Xenos Ruins"]
        self.ch_resource2 = wx.ComboBox( self, wx.ID_ANY, u"Other", wx.DefaultPosition, wx.DefaultSize, ch_resource2Choices, 0 )
        gbSizer1.Add( self.ch_resource2, wx.GBPosition( 10, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        ch_resource3Choices = [u"Curative", u"Juvenat Compound", u"Toxin", u"Vivid Accessory", u"Exotic Compound"]
        self.ch_resource3 = wx.ComboBox( self, wx.ID_ANY, u"Organics", wx.DefaultPosition, wx.DefaultSize, ch_resource3Choices, 0 )
        gbSizer1.Add( self.ch_resource3, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        ch_resource4Choices = [u"Canyon", u"Cave Network", u"Crater", u"Mountain", u"Volcano", u"Glacier(ex)", u"Inland Sea(ex)",u"Perpetual Storm(ex)",u"Reef(ex)", u"Whirlpool(ex)"]
        self.ch_resource4 = wx.ComboBox( self, wx.ID_ANY, u"Landmark", wx.DefaultPosition, wx.DefaultSize, ch_resource4Choices, 0 )
        gbSizer1.Add( self.ch_resource4, wx.GBPosition( 10, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_resource1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_resource1, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_resource2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_resource2, wx.GBPosition( 11, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_resource3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_resource3, wx.GBPosition( 11, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.v_resource4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.v_resource4, wx.GBPosition( 11, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_output = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_BESTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
        gbSizer1.Add( self.m_output, wx.GBPosition( 12, 0 ), wx.GBSpan( 17, 4 ), wx.ALL|wx.EXPAND, 5 )

        
        self.SetSizer( gbSizer1 )
        self.Layout()

        # Connect Events
        self.btn_save.Bind( wx.EVT_BUTTON, self.save_colony )
        self.btn_load.Bind( wx.EVT_BUTTON, self.load_colony )
        self.btn_generate.Bind( wx.EVT_BUTTON, self.create_colony )
        self.btn_calc.Bind( wx.EVT_BUTTON, self.calculate )
        self.btn_status.Bind( wx.EVT_BUTTON, self.status_update )

        #upgrade values
        self.main_upgrades = [["Transport",0,0], ["Power",0,0],
        ["Water",0,0], ["Food & Distro",0,0], ["Communication",0,0]]
        self.supp_upgrades = [["Arbites Precinct",0,0], ["Eccl. Mission",0,0], ["Mechanicum Station",0,0],["Infantry Garrison",0,0],  ["Navy Station",0,0], ["Cultural Monument",0,0], ["Industrial Facility",0,0],["Personal Lodgings",0,0], ["Contacts",0,0], ["Trappings",0,0]]
        
        colony_chosen = False
        chosen_colony = ""
        #save history

    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def status_update( self, event):
        pass

    def save_colony( self, event ):
        c_name = self.v_name.GetValue()
        c_type = self.ch_types.GetString(self.ch_types.GetCurrentSelection())
        c_contracted = self.m_funded.IsChecked()
        c_profit = int((self.v_profit.GetValue()))
        c_size = int(self.v_profit.GetValue())
        c_comp = int (self.v_comp.GetValue())
        c_order = int (self.v_comp.GetValue())
        c_prod = int (self.v_comp.GetValue())
        c_piety = int (self.v_comp.GetValue())
        c_fraction = int (self.v_comp.GetValue())
        c_year = int (self.v_comp.GetValue())
        c_millenium = int (self.v_comp.GetValue())
        c_governour = self.m_gov.GetValue()
        c_personality = self.ch_personality.GetString(self.ch_personality.GetCurrentSelection())
        c_minerals = self.ch_resource1.GetString(self.ch_resource1.GetCurrentSelection())
        c_addresource = self.ch_resource2.GetString(self.ch_resource2.GetCurrentSelection())
        c_organics = self.ch_resource3.GetString(self.ch_resource3.GetCurrentSelection())
        c_special = self.ch_resource4.GetString(self.ch_resource4.GetCurrentSelection())
        c_mvalue = int (self.v_comp.GetValue())
        c_avalue = int (self.v_comp.GetValue())
        c_ovalue = int (self.v_comp.GetValue())
        c_svalue = int (self.v_comp.GetValue())
        c_representative = self.ch_representative.GetString(self.ch_representative.GetCurrentSelection())
        c_history = self.m_output.GetValue()

        params = (c_name, c_type, c_contracted, c_profit, c_size, c_comp, c_order, c_prod, c_piety, c_fraction, c_year, c_millenium, c_governour, c_personality, c_minerals, c_addresource, c_organics, c_special, c_mvalue, c_avalue, c_ovalue, c_svalue, c_history, c_representative)

        c.execute("INSERT OR REPLACE INTO colonies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)

        main_upgrades = self.main_upgrades
        for entry in main_upgrades:
            params = (entry[0], entry[1], entry[2], entry[3], self.v_name.GetValue())
            c.execute("INSERT OR REPLACE INTO main_upgrades VALUES(?,?,?,?", params)

        supp_upgrades = self.supp_upgrades
        for entry in supp_upgrades:
            params = (entry[0], entry[1], entry[2], entry[3], self.v_name.GetValue())
            c.execute("INSERT OR REPLACE INTO supp_upgrades VALUES(?,?,?,?", params)

        conn.commit()

    def load_colony( self, event ):
        #choose name from database ? or similar, name it "colony" for other uses in function
        self.colony_chosen = False
        c.execute("SELECT * FROM colonies")
        rows = c.fetchall()
        #get colonies
        colony_choices = []
        for row in rows:
            colony_choices.append(str(row[0]))
        #create choice list and dialog
        self.dialog = wx.Dialog(None, -1, 'Choose Colony', size=(200,200), style=wx.DEFAULT_DIALOG_STYLE & ~wx.RESIZE_BORDER)
        self.colonies = wx.Choice(self.dialog, -1, (-1, -1), choices = colony_choices)
        self.load_btn_choice = wx.Button( self.dialog, wx.ID_ANY, u"Load !", (100,0), wx.DefaultSize, 0 )
        self.load_btn_choice.Bind( wx.EVT_LEFT_DOWN, self.btn_load_dialog )
        self.dialog.ShowModal()
        #wait until colony chosen
        while self.colony_chosen is False:
            wx.MilliSleep(100)
            wx.GetApp().Yield()
        #update hidden values
        colony = self.chosen_colony
        i = 0
        j = 0
        for x in self.main_upgrades:
            c.execute("SELECT * FROM main_upgrades WHERE colony=? AND infrastructure=?", (colony,x[0]))
            main_upgrades = c.fetchall()
            self.main_upgrades[i] = main_upgrades
            i=i+1

        for x in self.supp_upgrades:
            c.execute("SELECT * FROM supp_upgrades WHERE colony=? AND upgrade=?", (colony,x[0]))
            supp_upgrades = c.fetchall()
            self.supp_upgrades[j] = supp_upgrades
            j=j+1

        #fill in other values
        # c.execute("SELECT * FROM colonies WHERE name=?",(colony,))
        c_name = rows[colony][0]
        self.v_name.SetValue(c_name)
        c_type = rows[colony][1]
        c_type_id = self.ch_types.FindString(c_type)
        self.ch_types.SetSelection(c_type_id)
        c_contracted = str(rows[colony][2])
        self.m_funded.SetValue(int(c_contracted))
        c_profit = str(rows[colony][3])
        self.v_profit.SetValue(c_profit)
        c_size = str(rows[colony][4])
        self.v_size.SetValue(c_size)
        c_comp = str(rows[colony][5])
        self.v_comp.SetValue(c_comp)
        c_order = str(rows[colony][6])
        self.v_order.SetValue(c_order)
        c_prod = str(rows[colony][7])
        self.v_prod.SetValue(c_prod)
        c_piety = str(rows[colony][8])
        self.v_piety.SetValue(c_piety)
        c_fraction = str(rows[colony][9])
        self.v_frac.SetValue(c_fraction)
        c_year = str(rows[colony][10])
        self.v_year.SetValue(c_year)
        c_millenium = str(rows[colony][11])
        self.v_mill.SetValue(c_millenium)
        c_governour = rows[colony][12]
        self.m_gov.SetValue(c_governour)
        c_personality = rows[colony][13]
        c_personality_id = self.ch_personality.FindString(c_personality)
        self.ch_personality.SetSelection(c_personality_id)
        c_minerals = rows[colony][14]
        c_minerals_id = self.ch_resource1.FindString(c_minerals)
        self.ch_resource1.SetSelection(c_minerals_id)
        c_addresource = rows[colony][15]
        c_addresource_id = self.ch_resource2.FindString(c_addresource)
        self.ch_resource2.SetSelection(c_addresource_id)
        c_organics = rows[colony][16]
        c_organics_id = self.ch_resource3.FindString(c_organics)
        self.ch_resource3.SetSelection(c_organics_id)
        c_special = rows[colony][17]
        c_special_id = self.ch_resource4.FindString(c_special)
        self.ch_resource4.SetSelection(c_special_id)
        c_mvalue = str(rows[colony][18])
        self.v_resource1.SetValue(c_mvalue)
        c_avalue = str(rows[colony][19])
        self.v_resource2.SetValue(c_avalue)
        c_ovalue = str(rows[colony][20])
        self.v_resource3.SetValue(c_ovalue)
        c_svalue = str(rows[colony][21])
        self.v_resource4.SetValue(c_svalue)
        c_history = rows[colony][22]
        self.m_output.SetValue(c_history)
        c_representative = rows[colony][23]
        c_representative_id = self.ch_representative.FindString(c_representative)
        self.ch_representative.SetSelection(c_representative_id)


    def btn_load_dialog(self, event):
        self.chosen_colony = self.colonies.GetCurrentSelection()
        self.dialog.EndModal(1)
        self.colony_chosen = True

    def create_colony( self, event ):
        c_name = self.v_name.GetValue()
        c_type = self.ch_types.GetString(self.ch_types.GetCurrentSelection())
        if c_type == "":
            c_type = random.choices(
                population=["Agricultural", "Industrial", "Research", "Ecclesiarchal"],
                weights=[0.25,0.25,0.25,0.25],
                k=1,
            )
            c_type = str(c_type[0])
        c_contracted = self.m_funded.IsChecked()
        try:
            c_profit = int((self.v_profit.GetValue()))
        except ValueError:
            c_profit = 1
        try:
            c_size = int(self.v_profit.GetValue())
        except ValueError:
            c_size = 1
        try:
            c_comp = int (self.v_comp.GetValue())
        except ValueError:
            c_comp = 1
        try:
            c_order = int (self.v_comp.GetValue())
        except ValueError:
            c_order = 1
        try:
            c_prod = int (self.v_comp.GetValue())
        except ValueError:
            c_prod = 1
        try:
            c_piety = int (self.v_comp.GetValue())
        except ValueError:
            c_piety = 1
        c_fraction = int (self.v_frac.GetValue())
        c_year = int (self.v_year.GetValue())
        c_millenium = int (self.v_mill.GetValue())
        c_governour = self.m_gov.GetValue()
        if c_governour == "Governour":
            c_governour = random.choices(
                population=["Theon", "Calgan","Pyotr","Arthur","Jed", "Katharina", "Aphesius", "Zhara", "Violet", "Antaria"],
                weights=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
                k=1,
            )
            c_governour = str(c_governour[0])
        c_personality = self.ch_personality.GetString(self.ch_personality.GetCurrentSelection())
        if c_personality == "":
            c_personality = random.choice(["Beloved", "Militarist", "Corrupt", "Idle", "Ambitious", "Zealous", "Patron", "Unlucky", "Administrator", "Cruel", "Spymaster", "Generalissimo", "Paranoid", "Mad", "Charitable", "Vainglorious", "Scholarly", "Avaricious"])
        c_representative = self.ch_representative.GetString(self.ch_representative.GetCurrentSelection())
        if c_representative == "Representative":
            c_representative = random.choice(["Satrap", "Judge", "Cardinal", "Colonist", "General", "Dynasty Member"])
        c_minerals = self.ch_resource1.GetString(self.ch_resource1.GetCurrentSelection())
        if c_minerals == "Minerals":
            c_minerals = random.choices(
                population=["Industrial","Ornamental","Radioactive","Exotic Material"],
                weights=[0.4,0.3,0.2,0.1],
                k=1,
            )
            c_minerals = str(c_minerals[0])
        c_addresource = self.ch_resource2.GetString(self.ch_resource2.GetCurrentSelection())
        if c_addresource == "Add.Resource":
            c_addresource = random.choices(
                population=["Archeotech Cache", "Minerals", "Organic Compound", "Xenos Ruins"],
                weights=[0.1,0.4,0.4,0.1],
                k=1,
            )
            c_addresource = str(c_addresource[0])
        if c_addresource == "Xenos Ruins":
            c_addresource = random.choices(
                population=["Unknown Species","Eldar","Egarian","Yu'Vath","Ork","Kroot"],
                weights=[0.4,0.2,0.1,0.1,0.1,0.1],
                k=1,
            )
            c_addresource = str(c_addresource[0])
        c_organics = self.ch_resource3.GetString(self.ch_resource3.GetCurrentSelection())
        if c_organics == "Organics":
            c_organics = random.choices(
                population=["Curative", "Juvenat Compound", "Toxin", "Vivid Accessory", "Exotic Compound"],
                weights=[0.2,0.2,0.2,0.3,0.1],
                k=1,
            )
            c_organics = str(c_organics[0])
        c_special = self.ch_resource4.GetString(self.ch_resource4.GetCurrentSelection())
        if c_special == "Landmark":
            c_special = random.choices(
                population=["Canyon","Cave Network","Crater","Mountain","Volcano","Exceptional"],
                weights=[0.20,0.15,0.10,0.20,0.10,0.25],
                k=1,
            )
            c_special = str(c_special[0])
        if c_special == "Exceptional":
            c_special = random.choice(["Glacier(ex)","Inland Sea(ex)","Perpetual Storm(ex)","Reef(ex)","Whirlpool(ex)"])
        try:
            c_mvalue = int (self.v_comp.GetValue())
        except ValueError:
            c_mvalue = random.randint(1,100)
        try:
            c_avalue = int (self.v_comp.GetValue())
        except ValueError:
            c_avalue = random.randint(1,100)
        try:
            c_ovalue = int (self.v_comp.GetValue())
        except ValueError:
            c_ovalue = random.randint(1,100)
        try:
            c_svalue = int (self.v_comp.GetValue())
        except ValueError:
            c_svalue = random.randint(1,100)
        c_history = self.m_output.GetValue()
        params = (c_name, c_type, c_contracted, c_profit, c_size, c_comp, c_order, c_prod, c_piety, c_fraction, c_year, c_millenium, c_governour, c_personality, c_minerals, c_addresource, c_organics, c_special, c_mvalue, c_avalue, c_ovalue, c_svalue, c_history, c_representative)
        c.execute("INSERT OR REPLACE INTO colonies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
        conn.commit()

    def calculate( self, event ):
        pass

    def __del__( self ):
        pass
        

class Navigation(wx.Panel): 
    continue_travel = True

    def __init__(self, parent): 
        super(Navigation, self).__init__(parent) 

        # panel 1
        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.vi_nav = wx.lib.intctrl.IntCtrl(self)
        self.vi_nav.SetMaxSize(wx.Size(40, -1))

        gbSizer1.Add(
            self.vi_nav, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )
        
        self.vi_nav_mod = wx.lib.intctrl.IntCtrl(self)
        self.vi_nav_mod.SetMaxSize(wx.Size(40, -1))

        gbSizer1.Add(
            self.vi_nav_mod, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )

        self.vi_psy = wx.lib.intctrl.IntCtrl(self)
        self.vi_psy.SetMaxSize(wx.Size(40, -1))

        gbSizer1.Add(
            self.vi_psy, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )

        self.vi_psy_mod = wx.lib.intctrl.IntCtrl(self)
        self.vi_psy_mod.SetMaxSize(wx.Size(40, -1))

        gbSizer1.Add(
            self.vi_psy_mod, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )

        self.vl_nav_mod = wx.StaticText(
            self, wx.ID_ANY, u"Modifiers", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.vl_nav_mod.Wrap(-1)

        gbSizer1.Add(self.vl_nav_mod, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.vl_psy_mod = wx.StaticText(
            self, wx.ID_ANY, u"Modifiers", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.vl_psy_mod.Wrap(-1)

        gbSizer1.Add(self.vl_psy_mod, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.vl_psy = wx.StaticText(
            self, wx.ID_ANY, u"Psyniscience", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.vl_psy.Wrap(-1)

        gbSizer1.Add(self.vl_psy, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.vl_nav = wx.StaticText(
            self, wx.ID_ANY, u"Navigation", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.vl_nav.Wrap(-1)

        gbSizer1.Add(self.vl_nav, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox7 = wx.CheckBox(
            self, wx.ID_ANY, u"Component", wx.DefaultPosition, wx.DefaultSize, 0
        )
        gbSizer1.Add(self.m_checkBox7, wx.GBPosition(4, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox8 = wx.CheckBox(
            self, wx.ID_ANY, u"Charted ?", wx.DefaultPosition, wx.DefaultSize, 0
        )
        gbSizer1.Add(self.m_checkBox8, wx.GBPosition(4, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox9 = wx.CheckBox(
            self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0
        )
        gbSizer1.Add(self.m_checkBox9, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox10 = wx.CheckBox(
            self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0
        )
        gbSizer1.Add(self.m_checkBox10, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btn_start_nav = wx.Button(
            self, wx.ID_ANY, u"Forward !", wx.DefaultPosition, wx.DefaultSize, 0
        )
        gbSizer1.Add(
            self.btn_start_nav, wx.GBPosition(6, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )
        self.btn_cont_nav = wx.Button(
            self, wx.ID_ANY, u"Onwards !", wx.DefaultPosition, wx.DefaultSize, 0
        )
        gbSizer1.Add(
            self.btn_cont_nav, wx.GBPosition(6, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )
        self.btn_abort_nav = wx.Button(
            self, wx.ID_ANY, u"Emergency Exit !", wx.DefaultPosition, wx.DefaultSize, 0
        )
        gbSizer1.Add(
            self.btn_abort_nav, wx.GBPosition(6, 2), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )
        self.btn_load_stats = wx.Button(
            self, wx.ID_ANY, u"Load Navigator", wx.DefaultPosition, wx.DefaultSize, 0
        )
        gbSizer1.Add(
            self.btn_load_stats, wx.GBPosition(6, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )
        self.m_textCtrl5 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,style= wx.TE_MULTILINE|wx.VSCROLL|wx.TE_READONLY
        )
        self.m_textCtrl5.Enable(True)

        gbSizer1.Add(
            self.m_textCtrl5,
            wx.GBPosition(7, 0),
            wx.GBSpan(20, 4),
            wx.ALL | wx.EXPAND,
            5,
        )

        ch_styleChoices = [
            wx.EmptyString,
            u"Safety First",
            u"Gotta go Fast",
            u"Balance",
        ]
        self.ch_style = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_styleChoices, 0
        )
        self.ch_style.SetSelection(0)
        gbSizer1.Add(
            self.ch_style, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )

        ch_routeChoices = [
            wx.EmptyString,
            u"Tunnel",
            u"Stable",
            u"Unstable",
            u"Problematic",
            u"Warp Storm",
        ]
        self.ch_route = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_routeChoices, 0
        )
        self.ch_route.SetSelection(0)
        gbSizer1.Add(
            self.ch_route, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )

        ch_astroChoices = [
            wx.EmptyString,
            u"Shining",
            u"Visible",
            u"Shrouded",
            u"Obscured",
            u"Hidden",
        ]
        self.ch_astro = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_astroChoices, 0
        )
        self.ch_astro.SetSelection(0)
        gbSizer1.Add(
            self.ch_astro, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5
        )

        self.vl_warp_time = wx.StaticText(
            self, wx.ID_ANY, u"Warptime", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.vl_warp_time.Wrap(-1)

        gbSizer1.Add(self.vl_warp_time, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.vl_disparity = wx.StaticText(
            self, wx.ID_ANY, u"Disparity", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.vl_disparity.Wrap(-1)

        gbSizer1.Add(self.vl_disparity, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.vi_warp_time = wx.lib.intctrl.IntCtrl(self)
        gbSizer1.Add(
            self.vi_warp_time,
            wx.GBPosition(3, 1),
            wx.GBSpan(1, 1),
            wx.ALL | wx.EXPAND,
            5,
        )

        self.vi_disparity = wx.lib.intctrl.IntCtrl(self)
        gbSizer1.Add(self.vi_disparity, wx.GBPosition(3, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.SetSizer(gbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_start_nav.Bind(wx.EVT_LEFT_DOWN, self.start_flight)
        self.btn_cont_nav.Bind(wx.EVT_LEFT_DOWN, self.cont_flight)
        self.btn_abort_nav.Bind(wx.EVT_LEFT_DOWN, self.abort_flight)
        self.btn_load_stats.Bind(wx.EVT_LEFT_DOWN, self.load_stats)
        self.vi_nav.Bind(wx.EVT_CHAR, self.onChar)
        self.vi_psy.Bind(wx.EVT_CHAR, self.onChar)
        self.vi_nav_mod.Bind(wx.EVT_CHAR, self.onChar)
        self.vi_psy_mod.Bind(wx.EVT_CHAR, self.onChar)


    def load_stats(self, e):
        self.vi_nav.LoadFile(filename="navigator/nav")
        self.vi_nav_mod.LoadFile( filename="navigator/nav_mod")
        self.vi_psy.LoadFile( filename="navigator/psy")
        self.vi_psy_mod.LoadFile( filename="navigator/psy_mod")


    def __del__(self):
        pass

    def onChar(self, event):
        key = event.GetKeyCode()
        try:
            character = chr(key)
        except ValueError:
            character = ""  # arrow keys will throw this error
        acceptable_characters = "1234567890."
        if (
            character in acceptable_characters
            or key == 13
            or key == 314
            or key == 316
            or key == 8
            or key == 127
        ):  # 13 = enter, 314 & 316 = arrows, 8 = backspace, 127 = del
            event.Skip()
            return

        else:
            return False

    # Virtual event handlers, overide them in your derived class
    def cont_flight(self, event):
        self.continue_travel = True

    def abort_flight(self, event):
        # Emergency Exit
        pass


    def start_flight(self, event):
        succ = 0
        # get data
        nav = int(self.vi_nav.GetValue())
        psy = int(self.vi_psy.GetValue())
        nav_mod = int(self.vi_nav_mod.GetValue())
        psy_mod = int(self.vi_psy_mod.GetValue())
        check1 = self.m_checkBox7.GetValue()
        check2 = self.m_checkBox8.GetValue()
        check3 = self.m_checkBox9.GetValue()
        check4 = self.m_checkBox10.GetValue()
        style = self.ch_style.GetSelection()

        if self.ch_astro.GetSelection() != 0:
            obscured_state = self.ch_astro.GetSelection()
        else:
            obscured_state = random.choices(
                population=["Shining", "Visible", "Shrouded", "Obscured", "Hidden"],
                weights=[0.1, 0.50, 0.20, 0.15, 0.05],
                k=1,
            )


        if self.ch_route.GetSelection() !=0:
            stability = self.ch_route.GetSelection()
        else:
            stability = random.choices(
                population=[
                    "Tunnel",
                    "Stable",
                    "Unstable",
                    "Problematic",
                    "Warp Storm",
                ],
                weights=[0.05, 0.45, 0.3, 0.15, 0.05],
                k=1,
            )
        if stability == 1:
            disparity = 0.5
            nav_mod += 30
        if stability == 2:
            disparity = 10
            nav_mod += 10
        elif stability == 3:
            disparity = 15
            nav_mod -= 10
        elif stability == 4:
            disparity = 20
            nav_mod -= 30
        elif stability == 5:
            disparity = 60
            nav_mod -= 50
        else:
            disparity = 10
        
        if stability == 5 and obscured_state < 5:
            obscured_state +=1

        if self.vi_disparity.GetValue() != 0:
            disparity = self.vi_disparity.GetValue()
        else:
            if obscured_state == 1:
                disparity -= 5
                psy_mod += 30
            elif obscured_state == 2:
                disparity += 0
                psy_mod += 10
            elif obscured_state == 3:
                disparity += 2
                psy_mod -= 10
            elif obscured_state == 4:
                disparity += 5
                psy_mod -= 30
            elif obscured_state == 5:
                disparity += 10
                psy_mod -= 50

        if check2 is True:
            nav_mod += 10
        else:
            nav_mod -=10
        warp_time = self.vi_warp_time.GetValue()
        if warp_time == 0:
            self.m_textCtrl5.ChangeValue("Error: Missing Entries\n")
            return
        # while not enough successes
        need_succ = int(float(warp_time // 10))
        horror = 0
        if need_succ == 0:
            need_succ = 1
        need_succ_start = need_succ
        self.m_textCtrl5.AppendText("===============================\n")
        time_warp = 0
        while need_succ > succ:
            horror = 0
            # roll psy & spend on speed and bonus
            astro_roll = random.randint(0, 99) + psy + psy_mod - 100
            if astro_roll >= 0:
                astro_roll = (astro_roll // 10) + 1
            else:
                astro_roll = (astro_roll // 10) - 1
            if style == 0:
                style = "Balance"
            if style == "Gotta go Fast":
                while astro_roll != 0 and horror != 5:
                    if astro_roll < 0:
                        horror += 1
                        astro_roll += 1
                    elif astro_roll > 1:
                        disparity -= int(disparity / 8)
                        astro_roll -= 2
                    else:
                        nav_mod += 10
                        astro_roll = 0
            elif style == "Safety First":
                if astro_roll >= 0:
                    nav_mod += astro_roll * 10
                else:
                    while astro_roll < 0:
                        disparity += 2
                        astro_roll += 1
            else:
                while astro_roll > 1:
                    astro_roll -= 2
                    disparity -= int(disparity / 8)
                    nav_mod += 10
                while astro_roll < -1 and horror < 6:
                    astro_roll += 2
                    disparity += 2
                    horror += 1
            if astro_roll != 0 and horror == 5:
                nav_mod += astro_roll * 10
            # roll nav & spend on avoiding horrors
            nav_roll = random.randint(0, 99) + nav + nav_mod - 100
            if nav_roll >= 0:
                nav_roll = (nav_roll // 10) + 1
            else:
                nav_roll = (nav_roll // 10) - 1
            if style == "Gotta go Fast":
                if -6 < nav_roll <= 0:
                    horror += nav_roll * -1
                    nav_roll = 0
                elif nav_roll >= 0:
                    need_succ -= nav_roll
                else:
                    horror = 5
                    need_succ -= nav_roll
            elif style == "Safety First":
                while nav_roll < 0 and horror < 5:
                    nav_roll += 1
                    horror += 1
                while horror > 0 and nav_roll > 0:
                    horror -= 1
                    nav_roll -= 1
                need_succ -= nav_roll
            else:
                while nav_roll != 0:
                    if nav_roll > 1 and horror > 0:
                        need_succ -= 1
                        horror -= 1
                        nav_roll -= 2
                    elif nav_roll == 1 and horror > 0:
                        horror -= 1
                        nav_roll -= 1
                    elif nav_roll > 0 and horror == 0:
                        need_succ -= 1
                        nav_roll -= 1
                    elif nav_roll < -1 and horror < 5:
                        horror += 1
                        need_succ += 1
                        nav_roll += 2
                    elif nav_roll < -1 and horror == 5:
                        need_succ -= nav_roll
                        nav_roll = 0
                    elif nav_roll == -1 and horror < 5:
                        horror += 1
                        nav_roll = 0
                    else:
                        need_succ += 1
                        nav_roll = 0
            if horror == 1:
                self.m_textCtrl5.AppendText("Aetheric Breakers: ")
                roll = (random.randint(0, 99) + nav + nav_mod - 100) // 10
                if roll <= 0:
                    self.m_textCtrl5.AppendText("The pilot manages to dodge.")
                else:
                    roll = random.randint(1, 10)
                    self.m_textCtrl5.AppendText(
                        "The ship takes "
                        + str(roll + 14)
                        + " damage, ignoring shields."
                    )
                    if roll == 10:
                        self.m_textCtrl5.AppendText(
                            "A random exterior component, suffers a critical hit."
                        )
            if horror == 2:
                self.m_textCtrl5.AppendText("Warp Sickness: ")
                roll = random.randint(1, 3)
                if roll == 1:
                    self.m_textCtrl5.AppendText("Illness: ")
                    roll = random.randint(1, 10)
                    self.m_textCtrl5.AppendText(
                        str(roll)
                        + " Crew is lost to sickness until the ship leaves the warp and medical assistance is given. 1 point is permanently lost if left longer than 30 days."
                    )
                elif roll == 2:
                    self.m_textCtrl5.AppendText("Insanity: ")
                    roll = random.randint(1, 10)
                    self.m_textCtrl5.AppendText(
                        str(roll)
                        + " Crew is lost to madness until the ship leaves the warp. Riots may break out and the effects may worsen if this was an early event. 1 point is permanently lost."
                    )
                else:
                    self.m_textCtrl5.AppendText("Corruption: ")
                    roll = random.randint(2, 10)
                    self.m_textCtrl5.AppendText(
                        str(roll)
                        + " Crew is lost to corruption. Every point loss is permanent and they need to be eradicated fast. Ship may become Haunted (p.198) and Death Cults may hunt survivors"
                    )
            if horror == 3:
                self.m_textCtrl5.AppendText("Warp Storm: ")
                self.m_textCtrl5.AppendText(
                    "The ship passes a Warpstorm. Disparity might be affected... "
                )
                affect_time = random.choices(
                    population=(5, 10, 15, 20), weights=(0.4, 0.3, 0.2, 0.1),k=1
                )
                disparity += affect_time[0]
            if horror == 4:
                self.m_textCtrl5.AppendText("Warp Horror: \n")
                self.m_textCtrl5.AppendText(
                    "The Ship is chased by a young Void Kraken. \n Stern Chase (p.216). S3, WS 50, 1d10+14, Crit 5, Armor 0, Hull 50 "
                )
            if horror == 5:
                self.m_textCtrl5.AppendText("Daemonic Incursion: ")
                x = 4
                result = 0
                while x > 3:
                    x = random.randint(0, 9)
                    result += 1
                    hull = random.randint(1, 5)
                self.m_textCtrl5.AppendText(
                    "The Ship takes "
                    + str(hull)
                    + "Hull, Crew and Moral damage. Each player takes"
                    + str(result)
                    + " unabsorbable damage."
                )
            self.m_textCtrl5.AppendText("\n"+ str(need_succ) + " successes left\n")
            time_warp += 1
            #wait for confiramtion
            self.continue_travel = False
            while self.continue_travel is False:
                wx.MilliSleep(100)
                wx.GetApp().Yield()
            # output result in textctrl
            # min and max disparities
        if stability == "Tunnel":
            disparity = 0.5
        elif stability == 5 and disparity < 30:
            disparity = 30
        if time_warp > 1:
            warp_time += ((time_warp*time_warp) // 10)
        self.m_textCtrl5.AppendText("Astronomicon: " + str(obscured_state))
        self.m_textCtrl5.AppendText(" - Disparity: "  + str(disparity)  +"\n")
        self.m_textCtrl5.AppendText(
            "Route: " + str(stability) + " - Actual Warp Time: " + str(warp_time)+"\n"
        )
        self.m_textCtrl5.AppendText("Realtime: " + str(warp_time * disparity)+"\n")
        fraction = ((warp_time *disparity)*1000)//356
        millenium = 0
        while fraction > 999:
            fraction -= 1000
            millenium += 1 
        self.m_textCtrl5.AppendText("Time passed: "+str(fraction)+"." + str(millenium)+"\n")


if __name__ == "__main__":
    app = wx.App(False)
    frame = RT_Tools(parent=None)
    frame.Show()
    app.MainLoop()
