# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import random
from wx.lib.intctrl import IntCtrl
import pickle

###########################################################################
## Class MyFrame1
###########################################################################


class MyFrame1(wx.Frame):
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
        super(MyFrame1, self).__init__(parent, size = (490,720))
        self.InitUI()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
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
        win = MyFrame1(None)
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
   def __init__(self, parent): 
      super(Colonies, self).__init__(parent) 
      text = wx.TextCtrl(self, style = wx.TE_MULTILINE, size = (250,150)) 
        

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
    frame = MyFrame1(parent=None)
    frame.Show()
    app.MainLoop()
