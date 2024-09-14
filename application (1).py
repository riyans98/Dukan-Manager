#class namings start at line 894 and app class starts at 1113 and end at 1213
#menu class ends at line 1083
#builder string starts at line 26 and ends at 894,menu starts at 398 and ends at 549
import kivy
import os
from datetime import datetime
import xlsxwriter
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup 
from kivy.core.window import Window 
Builder.load_string('''
<Signin>:
	canvas:
    	Color:
    		rgb: (255/255,69/255,0/255)
    	RoundedRectangle:
    		size:(720,750)
    		pos:(0,950)
    		radius:[70]
    	#white curve
    	Color:
    		rgb: (255/255,255/255,255/255)
    	Ellipse:
    		angle_start:180
    		angle_end:360
    		pos: 375.24, 740
    		size: 751,410
    	#red curve
    	Color:
    		rgb: (255/255,69/255,0/255)
    	Ellipse:
    		angle_start:0
    		angle_end:180
    		pos: -375.24, 740
    		size: 751,410    		
   	#logo
    	Color:
    		rgb: (255/255,69/255,0/255)
    	RoundedRectangle:
    		size:(300,300)
    		pos:(210,1130)
    		radius:[30]
    	#blue
    	Color:
    		rgb: (0/255,191/255,255/255)
    	RoundedRectangle:
    		size:(180,140)
    		pos:(240,1137)
    		radius:[43]
    	#holes
    	Color:
    		rgb: (255/255,228/255,181/255)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(359,1118)
    		size:(25,23)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(272,1118)
    		size:(25,23)
    	#side rectangle blue
    	Color:
    		rgb: (0/255,191/255,255/255)
    	RoundedRectangle:
    		size:(22,90)
    		pos:(240,1165)
    		radius:[13]
    	#handle blue
    	Color:
    		rgb: (0/255,191/255,255/255)
    	RoundedRectangle:
    		size:(65,22)
    		pos:(394,1250)
    		radius:[10]
    	#centre red
    	Color:
    		rgb: (255/255,69/255,0/255)
    	RoundedRectangle:
    		size:(141,190)
    		pos:(260,1158)
    		radius:[45]    	
    	#bag color
    	Color:
    		rgb: (235/255,155/255,55/255)
    	RoundedRectangle:
    		size:(99,16)
    		pos:(279,1184)
    		radius:[7.5]
    	#triangle
    	Color:
    		rgb:(235/255,155/255,55/255)
    	Ellipse:
    		segments:3
    		pos:(270,1131)
    		size:(116,250)
    	#tempsq
    	Color:
    		rgb: (255/255,69/255,0/255)
    	Rectangle:
    		size:(67,121)
    		pos:(293,1265)
    	#handles of bag
    	Color:
    		rgb: (235/255,155/255,55/255)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(299,1220)
    		size:(58,89)
    	Color:
    		rgb: (255/255,69/255,0/255)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(309,1220)
    		size:(39,79)
    	Color:
    		rgb: (255/255,69/255,0/255)
    	Rectangle:
    		size:(60,70)
    		pos:(208,1249)
    	Color:
    		rgb: (235/255,155/255,55/255)
    	Rectangle:
    		size:(60,70)
    		pos:(298,1199)
    	#holes
    	Color:
    		rgb: (255/255,255/255,255/255)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(339,1250)
    		size:(10,10)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(305,1250)
    		size:(10,10)
    	Ellipse:
    		angle_start:135
    		angle_end:225
    		pos:(287.5,1218)
    		size:(80,80)
    	Color:
    		rgb: (235/255,155/255,55/255)
    	Ellipse:
    		angle_start:135
    		angle_end:225
    		pos:(292.5,1223)
    		size:(70,70)
    unm:unm_input
    pas:pas_input
	FloatLayout:
		MButton:
			text: 'Get Registered'
			background_normal:''
			font_size:self.width/10
            size_hint:0.82,0.08
            border:0,0,0,0
            pos_hint:{'x':.1,'y':.13}
            on_press: root.manager.current = 'rg'
        TextInput:
			id:unm_input
			multiline:False
			hint_text:'Enter Your Username'
			size_hint:.85,0.04
            pos_hint:{'x':.08,'y':.47}
            focus:True
            on_text_validate: unm_input.focus=True
		TextInput:
			id:pas_input
			hint_text:'Enter Your Password'
			multiline:False
			size_hint:.85,0.04
			focus:True
			on_text_validate: pas_input.focus=True
            pos_hint:{'x':.08,'y':.42}
		AsButton:
			text:'Login'
			size_hint:0.25,0.05
            pos_hint:{'x':.7,'y':.3}
            on_press:pas_input.focus=True
            on_press:pas_input.text='' 
            on_press:unm_input.focus=True
            on_press:unm_input.text='' 
			on_press: root.manager.current = 'menu' if unm_input.text==app.logunm(unm_input.text) and pas_input.text==app.logpas(unm_input.text,pas_input.text) else 'sg'
        
<Register>:
	canvas:
    	Color:
    		rgb: (240/255,0/255,0/255)
    	RoundedRectangle:
    		size:(720,750)
    		pos:(0,950)
    		radius:[70]
    	Color:
    		rgb: (255/255,255/255,255/255)
    	Ellipse:
    		angle_start:180
    		angle_end:360
    		pos: 375.5, 740
    		size: 751,410
    	Color:
    		rgb: (240/255,0/255,0/255)
    	Ellipse:
    		angle_start:0
    		angle_end:180
    		pos: -375.5, 740
    		size: 751,410
    		#logo
    	Color:
    		rgb: (240/255,0/255,0/255)
    	RoundedRectangle:
    		size:(300,300)
    		pos:(210,1130)
    		radius:[30]
    	#blue
    	Color:
    		rgb: (70/255,110/255,180/255)
    	RoundedRectangle:
    		size:(180,140)
    		pos:(240,1140)
    		radius:[43]
    	#holes
    	Color:
    		rgb: (70/255,110/255,180/255)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(357,1118)
    		size:(23,23)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(274,1118)
    		size:(23,23)
    	#side rectangle blue
    	Color:
    		rgb: (70/255,110/255,180/255)
    	RoundedRectangle:
    		size:(22,90)
    		pos:(240.5,1185)
    		radius:[13]
    	#handle blue
    	Color:
    		rgb: (70/255,110/255,180/255)
    	RoundedRectangle:
    		size:(85,22)
    		pos:(399,1250)
    		radius:[10]
    	#centre red
    	Color:
    		rgb: (240/255,0/255,0/255)
    	RoundedRectangle:
    		size:(141,190)
    		pos:(260,1158)
    		radius:[45]
    	
    	#bag color
    	Color:
    		rgb: (235/255,155/255,55/255)
    	RoundedRectangle:
    		size:(99,16)
    		pos:(279,1184)
    		radius:[7.5]
    	
    	#triangle
    	Color:
    		rgb:(235/255,155/255,55/255)
    	Ellipse:
    		segments:3
    		pos:(270,1131)
    		size:(116,250)
    	#tempsq
    	Color:
    		rgb: (240/255,0/255,0/255)
    	Rectangle:
    		size:(67,121)
    		pos:(293,1265)
    	#handles of bag
    	Color:
    		rgb: (235/255,155/255,55/255)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(299,1220)
    		size:(58,89)
    	Color:
    		rgb: (240/255,0/255,0/255)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(309,1220)
    		size:(39,79)
    	Color:
    		rgb: (235/255,155/255,55/255)
    	Rectangle:
    		size:(60,70)
    		pos:(298,1199)
    	#holes
    	Color:
    		rgb: (255/255,255/255,255/255)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(339,1250)
    		size:(10,10)
    	Ellipse:
    		angle_start:0
    		angle_end:360
    		pos:(305,1250)
    		size:(10,10)
    	Ellipse:
    		angle_start:135
    		angle_end:225
    		pos:(287.5,1218)
    		size:(80,80)
    	Color:
    		rgb: (235/255,155/255,55/255)
    	Ellipse:
    		angle_start:135
    		angle_end:225
    		pos:(292.5,1223)
    		size:(70,70)
	name:"rg"
	nm:str(nm_input)
	unm:unm_input
	pas:pas_input
	FloatLayout:
		TextInput:
			id:nm_input
			multiline:False
			hint_text:'Enter Your Name'
			size_hint:.85,0.04
            pos_hint:{'x':.08,'y':.52}
            focus:True
            on_text_validate: nm_input.focus=True
        TextInput:
			id:unm_input
			multiline:False
			hint_text:'Enter Your Username'
			size_hint:.85,0.04
            pos_hint:{'x':.08,'y':.47}
            focus:True
            on_text_validate: unm_input.focus=True
		TextInput:
			id:pas_input
			hint_text:'Enter Your Password'
			multiline:False
			size_hint:.85,0.04
			focus:True
			on_text_validate: pas_input.focus=True
            pos_hint:{'x':.08,'y':.42}
		AsButton:
			text:'Save'
			size_hint:0.25,0.05
            pos_hint:{'x':.7,'y':.3}
            on_press:pas_input.focus=True
            on_press:pas_input.text='' 
            on_press:unm_input.focus=True
            on_press:unm_input.text='' 
            on_press:nm_input.focus=True
            on_press:nm_input.text='' 
			on_press: app.rgstr(nm_input.text,pas_input.text,unm_input.text);root.manager.current = 'menu'
<MenuScreen>:
    pnm:pnm_input
    qpnm:qpnm_input
    npnm:npnm_input
    canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
    	#badawala(bichwala)
    	Color:
    		rgb: (122.5/255,122.5/255,122.5/255)
    	RoundedRectangle:
    		size:(660,419)
    		pos:(30,503)
    		radius:[50]
    	Color:
    		rgb: (255/255,255/255,255/255)
    	RoundedRectangle:
    		size:(657,425)
    		pos:(30,506)
    		radius:[50]
    	#topmost grey(chotawala)
    	Color:
    		rgb: (122.5/255,122.5/255,122.5/255)
    	RoundedRectangle:
    		size:(660,259)
    		pos:(31,953)
    		radius:[50]
    	Color:
    		rgb: (255/255,255/255,255/255)
    	RoundedRectangle:
    		size:(657,267)
    		pos:(31,955.8)
    		radius:[50]
    	#lowest rectangle
    	Color:
    		rgb: (122.5/255,122.5/255,122.5/255)
    	RoundedRectangle:
    		size:(660,409)
    		pos:(31,50)
    		radius:[50]
    	Color:
    		rgb: (255/255,255/255,255/255)
    	RoundedRectangle:
    		size:(657,415)
    		pos:(31,53.3)
    		radius:[50]
    name:"menu"
    FloatLayout:
        RgLabel:
        	text:'Welcome to Dukan Manager'
        	size_hint:.393,.05
        	font_size:self.width/5.5
        	pos_hint:{'x':.32,'y':.942}
        RButton:
            text: 'New Product'
            size_hint:0.36,0.13
            pos_hint:{'x':.1,'y':.17}
            on_press: root.manager.current = 'add_staff'
        RButton:
        	text:'Update data'
        	size_hint:0.36,0.13
            pos_hint:{'x':.53,'y':.17}
            on_press: root.manager.current = 'updatec'
		TextInput:
			id:pnm_input
			hint_text:'Product Name'
			hint_font_size:99
			font_size:34
			focus:True
			size_hint:0.79,0.05
			multiline:False
			on_text_validate: pnm_input.focus=True
        	pos_hint: {"x":0.08, "y":.56}
        AsButton:
        	text:'Get all details.'
        	size_hint:0.37,0.123
        	pos_hint: {"x":0.078, "y":.41}
        	on_press:root.manager.get_screen('bftc').pnm.text=root.pname(pnm_input.text);root.manager.get_screen('bftc').pac.text=root.pac(pnm_input.text);root.manager.get_screen('bftc').pas.text=root.pas(pnm_input.text);root.manager.get_screen('bftc').psp.text=root.psp(pnm_input.text);root.manager.get_screen('bftc').pcp.text=root.pcp(pnm_input.text);root.manager.get_screen('bftc').pmi.text=root.pmi(pnm_input.text);root.manager.get_screen('bftc').pme.text=root.pme(pnm_input.text);root.manager.get_screen('bftc').pbft.text=root.pbft(pnm_input.text);root.manager.get_screen('bftc').plos.text=root.plos(pnm_input.text);root.manager.get_screen('bftc').pamlft.text=root.pamlft(pnm_input.text);root.manager.current='bftc'
        	on_release:pnm_input.focus=True;pnm_input.text='' 
        MLabel:
        	text:"Update Today's sales"
        	size_hint:0.47,0.1
        	pos_hint: {"x":0.035, "y":.815}
        MLabel:
        	text:"Edit and Manage"
        	size_hint:0.47,0.1
        	pos_hint: {"x":0.0185, "y":.273}
        MLabel:
        	text:"Current status of product"
        	size_hint:0.47,0.1
        	pos_hint: {"x":0.055, "y":.593}
        TextInput:
			id:npnm_input
			hint_text:'Product Name'
			font_size:32
			focus:True
			size_hint:0.78,0.055
			multiline:False
			on_text_validate:npnm_input.focus=True
        	pos_hint: {"x":0.0919, "y":.785}
        TextInput:
			id:qpnm_input
			hint_text:'Quantity'
			font_size:32
			focus:True
			input_filter:'int'
			size_hint:0.22,0.055
			multiline:False
			on_text_validate: qpnm_input.focus=True
        	pos_hint: {"x":0.091, "y":.723}
        AsButton:
        	text:'Update'
        	size_hint:0.35,0.05
        	on_press:qpnm_input.focus=True
            on_press:qpnm_input.text='' 
            on_press:npnm_input.focus=True
            on_press:npnm_input.text='' 
            on_press:root.updateas(npnm_input.text,qpnm_input.text)
        	pos_hint: {"x":0.514, "y":.723}
		ScrollView:
	        size_hint_y:None
	        size_hint_x:.4
	        size:38,170
	        pos_hint:{'x':.48,'y':.407}
	        do_scroll_x: False
	        do_scroll_y: True
	        scroll_type:['bars', 'content']
	        bar_width: 3	        
	        BoxLayout:
	            orientation: 'vertical'
	            id: sv_box
	            size_hint_y: None
	            spacing:3
	            height: self.minimum_height
	            InfoLline:
	                SButton:
	                	text:'Benefit'
	                	on_press:pnm_input.focus=True
	                	on_press:pnm_input.text=''
	                	on_press:root.manager.get_screen('bftr').usr.text=root.benefit(pnm_input.text);root.manager.current='bftr'
	                	
	            InfoLline:
	                SButton:
	                	text: 'Money Invested'
	                	on_press:pnm_input.focus=True
	                	on_press:pnm_input.text='' 
	                	on_press:root.manager.get_screen('mir').usr.text=root.mi(pnm_input.text);root.manager.current = 'mir'
	            
	            InfoLline:
	                SButton:
	                	text: 'Money earned'
	                	on_press:pnm_input.focus=True
	                	on_press:pnm_input.text='' 
	                	on_press:root.manager.get_screen('mer').usr.text=root.me(pnm_input.text);root.manager.current = 'mer'
	            InfoLline:
	                SButton:
	                	text: 'Units Bought'
	                	on_press:pnm_input.focus=True
	                	on_press:pnm_input.text='' 
	                	on_press:root.manager.get_screen('amtr').usr.text=root.amt(pnm_input.text);root.manager.current = 'amtr'
	            InfoLline:
	                SButton:
	                	text: 'Units Sold'
	                	on_press:pnm_input.focus=True
	                	on_press:pnm_input.text='' 
	                	on_press:root.manager.get_screen('amtsr').usr.text=root.amts(pnm_input.text);root.manager.current = 'amtsr'
	            InfoLline:
	                SButton:
	                	text: 'Units left'
	                	on_press:pnm_input.focus=True
	                	on_press:pnm_input.text='' 
	                	on_press:root.manager.get_screen('amtsleft').usr.text=root.amtsleft(pnm_input.text);root.manager.current = 'amtsleft'
	            InfoLline:
	                SButton:
	                	text: 'Selling Price'
	                	on_press:pnm_input.focus=True
	                	on_press:pnm_input.text='' 
	                	on_press:root.manager.get_screen('selp').usr.text=root.sp(pnm_input.text);root.manager.current = 'selp'
	            InfoLline:
	                SButton:
	                	text: 'Cost Price'
	                	on_press:pnm_input.focus=True
	                	on_press:pnm_input.text='' 
	                	on_press:root.manager.get_screen('cop').usr.text=root.cp(pnm_input.text);root.manager.current = 'cop'
	    SButton:
            text: 'Excel file with normal data'
            size_hint:0.8,0.05
            pos_hint:{'x':.0917,'y':.11}
            on_press: app.excell();root.btn()
	    SButton:
            text: 'Excel file with all stats'
            size_hint:0.8,0.05
            pos_hint:{'x':.0917,'y':.05}
            on_press: root.excelll()
#save button of add pdct
<SButton@Button>:
	background_color:(0,0,0,0)
	background_normal:''
	canvas.before:
		Color:
			rgb:(90/255,144/255,255/255)
		RoundedRectangle:
			size:self.size
			pos:self.pos
			radius:[13]
<AsButton@Button>:
	background_color:(0,0,0,0)
	background_normal:''
	canvas.before:
		Color:
			rgb:(90/255,144/255,255/255)
		RoundedRectangle:
			size:self.size
			pos:self.pos
			radius:[35]
<Add_new_product>:
    name:"add_staff"
    namei: str(namei_input)
    amt:str(amt_input)
    cp:str(cp_input)
    amts:str(amts_input)
    sp:str(sp_input)
    canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
    FloatLayout:
        RgLabel:
        	text:'Add New Product'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
        TextInput:
            id: namei_input
            multiline: False
            hint_text: 'Name'
            size_hint:0.5,0.05
            pos_hint:{'x':.1,'y':.82}
            focus:True
        TextInput:
            id: amt_input
            hint_text:'Amount Bought'
            multiline: False
            size_hint:0.5,0.05
            input_filter:'int'
            pos_hint:{'x':.1,'y':.71}
            focus:True
        TextInput:
            id: cp_input
            multiline: False
            hint_text: 'Cost Price'
            size_hint:0.5,0.05
            pos_hint:{'x':.1,'y':.61}
            input_filter:'float'
            focus:True
        TextInput:
            id: amts_input
            input_filter:'int'
            multiline: False
            hint_text: 'Amount Sold'
            size_hint:0.5,0.05
            pos_hint:{'x':.1,'y':.51}
            focus:True
        TextInput:
            id: sp_input
            input_filter:'float'
            hint_text: 'Selling Price'
            multiline: False
            size_hint:0.5,0.05
            pos_hint:{'x':.1,'y':.41}
            focus:True
        AsButton:
			text:'Back'
			size_hint:(.25,.05)
			pos_hint:{'x':.7,'y':.2}
			on_release:root.manager.current='menu'
        AsButton:
            text: 'Save'
            size_hint:0.25,0.05
            pos_hint:{'x':.7,'y':.35}
            on_press: app.save(namei_input.text, amt_input.text,cp_input.text,amts_input.text,sp_input.text);root.manager.current = 'menu';namei_input.focus=True;namei_input.text='' ;amt_input.focus=True;amt_input.text='' ;cp_input.focus=True;cp_input.text='' ;amts_input.focus=True;amts_input.text='' ;sp_input.focus=True;sp_input.text='' 
<Updatepd>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	FloatLayout:
		nup:nup_input
		v:v_input
		RgLabel:
        	text:'Update Product'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		TextInput:
			id:nup_input
			multiline:False
			hint_text:'Enter product name'
			size_hint:0.8,0.05
            pos_hint:{'x':.1,'y':.65}
            focus:True
		TextInput:
			id:v_input
			hint_text:'Enter New Value'
			size_hint:0.8,0.05
            pos_hint:{'x':.1,'y':.55}
            multiline:False
            focus:True
        ScrollView:
	        size_hint_y:None
	        size_hint_x:.35
	        size:53,280
	        pos_hint:{'x':.6,'y':.25}
	        do_scroll_x: False
	        do_scroll_y: True
	        scroll_type:['bars', 'content']
	        bar_width: 5
	        BoxLayout:
	            orientation: 'vertical'
	            id: siv_box
	            spacing:3
	            size_hint_y:None
	            height:self.minimum_height
	            Infoline:
	                SButton:
	                	text:'Product Name'
	                	on_press: root.updatenm(nup_input.text,v_input.text);root.manager.current = 'menu';nup_input.focus=True;nup_input.text='';v_input.focus=True;v_input.text=''
	            Infoline:
	            	SButton:
	            		text:'Amount Bought'
	            		on_press: root.updateac(nup_input.text,v_input.text);root.manager.current = 'menu';nup_input.focus=True;nup_input.text='';v_input.focus=True;v_input.text=''
	            Infoline:
	            	SButton:
	            		text:'Amount Sold'
	            		on_press: root.updateas(nup_input.text,v_input.text);root.manager.current = 'menu';nup_input.focus=True;nup_input.text='';v_input.focus=True;v_input.text=''
	            Infoline:
	            	SButton:
	            		text:'Selling Price'
	            		on_press: root.updatesp(nup_input.text,v_input.text);root.manager.current = 'menu';nup_input.focus=True;nup_input.text='';v_input.focus=True;v_input.text=''
	            Infoline:
	            	SButton:
	            		text:'Cost Price'
	            		on_press: root.updatecp(nup_input.text,v_input.text);root.manager.current = 'menu';nup_input.focus=True;nup_input.text='';v_input.focus=True;v_input.text=''
        MLabel:
        	text:'Please enter correct product name and field.*'
        	pos_hint:{'x':-.025,'y':.23}
        AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.63,'y':.15}
			on_release:root.manager.current='menu'
<Popups>:
    FloatLayout:
        MLabel:
        	text:'Update Successful'
        	size_hint:0.1,0.1
        	pos_hint: {"x":0.9, "y":5.2} 
<Popus>:
    FloatLayout:
        Label:
        	text:'Excel file generated'
        	size_hint:0.1,0.1
        	pos_hint: {"x":0.9, "y":8.2}
<InfoLline>:
	size_hint_y:None
    orientation:'vertical'
    height:75
    spacing:35
<Infoline>:
    size_hint_y:None
    orientation:'horizontal'
    height:85
    spacing:65
<Bftc>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	pnm:pnm
	pac:pac
	pas:pas
	pcp:pcp
	psp:psp
	pmi:pmi
	pme:pme
	pbft:pbft
	plos:plos
	pamlft:pamlft
	FloatLayout:
		RgLabel:
        	text:'Product Details'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'yu'
			id:pnm
			size_hint:0.1,0.1
        	pos_hint: {"x":0.45, "y":0.85}
        
        MLabel:
			text:'yu'
			id:pac
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.8}
        MLabel:
			text:'yu'
			id:pas
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.75}
        MLabel:
			text:'yu'
			id:pcp
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.7}
        MLabel:
			text:'yu'
			id:psp
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.65}
        MLabel:
			text:'yu'
			id:pmi
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.6}
        MLabel:
			text:'yu'
			id:pme
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.55}
        MLabel:
			text:'yu'
			id:pbft
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.5}
        MLabel:
			text:'yu'
			id:plos
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.45}
        MLabel:
			text:'yu'
			id:pamlft
			size_hint:0.1,0.1
        	pos_hint: {"x":0.72, "y":0.4}
        MLabel:
			text:'Amount Bought'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.8}
        MLabel:
			text:'Amount Sold'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.75}
        MLabel:
			text:'Cost Price'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.7}
        MLabel:
			text:'Selling Price'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.65}
        MLabel:
			text:'Money Invested'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.6}
        MLabel:
			text:'Money Earned'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.55}
        MLabel:
			text:'Benefit'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.5}
        MLabel:
			text:'Loss'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.45}
        MLabel:
			text:'Amount left'
			size_hint:0.1,0.1
        	pos_hint: {"x":0.22, "y":0.4}
        AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.13}
			on_release:root.manager.current='menu'
<Bftrslt>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	usr:usr
	FloatLayout:
		RgLabel:
        	text:'Benefit of Product'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'dflt'
			id:usr
			size_hint:.1,.1
			pos_hint:{'x':.45,'y':.5}
		AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.15}
			on_release:root.manager.current='menu'
<Mirslt>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	usr:usr
	FloatLayout:
		RgLabel:
        	text:'Money Invested'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'hj'
			id:usr
			pos_hint:{'x':.01,'y':.0}
		AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.15}
			on_release:root.manager.current='menu'
<Merslt>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	usr:usr
	FloatLayout:
		RgLabel:
        	text:'Money Earned'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'uj'
			id:usr
			pos_hint:{'x':.01,'y':.0}
		AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.15}
			on_release:root.manager.current='menu'
<Amtrslt>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	usr:usr
	FloatLayout:
		RgLabel:
        	text:'Amount'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'ui'
			id:usr
			pos_hint:{'x':.01,'y':0}
		AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.15}
			on_release:root.manager.current='menu'
<Amtsrslt>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	usr:usr
	FloatLayout:
		RgLabel:
        	text:'Amount Sold'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'ui'
			id:usr
			pos_hint:{'x':.01,'y':.0}
		AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.15}
			on_release:root.manager.current='menu'
<Amtsleft>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	usr:usr
	FloatLayout:
		RgLabel:
        	text:'Amounts Left'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'uo'
			id:usr
			pos_hint:{'x':.01,'y':.0}
		AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.15}
			on_release:root.manager.current='menu'
<Sellingp>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	usr:usr
	FloatLayout:
		RgLabel:
        	text:'Selling Price'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'uo'
			id:usr
			pos_hint:{'x':.01,'y':.0}
		AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.15}
			on_release:root.manager.current='menu'
<Costp>:
	canvas:
    	Color:
    		rgb: (241/255,241/255,241/255)
    	Rectangle:
    		size:(1499,1499)
    		pos:(0,0)
    	Color:
    		rgb: (50/255,194/255,255/255)
    	RoundedRectangle:
    		size:(720,499)
    		pos:(0,1249)
    		radius:[50]
	usr:usr
	FloatLayout:
		RgLabel:
        	text:'Cost Price'
        	size_hint:.393,.05
        	font_size:self.width/4
        	pos_hint:{'x':.32,'y':.935}
		MLabel:
			text:'uo'
			id:usr
			pos_hint:{'x':.02,'y':.0}
		AsButton:
			text:'Back'
			size_hint:(.2,.05)
			pos_hint:{'x':.75,'y':.15}
			on_release:root.manager.current='menu'
<MLabel@Label>:
	color:(255/255,69/255,0/255)
<RgLabel@Label>:
	color:(255/255,235/255,0/255)
 
<RButton@Button>:
	background_color:(0,0,0,0)
	background_normal:''
	canvas.before:
		Color:
			rgb: (90/255,144/255,255/255)
		RoundedRectangle:
			size:self.size
			pos:self.pos
			radius:[58]
<MButton@Button>:
	background_color:(0,0,0,0)
	background_normal:''
	canvas.before:
		Color:
			rgb:(90/255,145/255,255/255)
		RoundedRectangle:
			size:self.size
			pos:self.pos
			radius:[58]
''')

class Signin(Screen):
	Window.size = (1050, 2100)
	Window.clearcolor=(255/255,255/255,255/255,0)
class Register(Screen):
    pass
class MenuScreen(Screen):
    def btn(self):
    	sho_popup()
    def pname(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg='Please enter product name'
    			elif b[i]==pnm:
    				hg=pnm
    			elif pnm not in b:
    				hg='Enter valid Product Name'
    		return hg
    	except Exception as e:
    		return 'Enter correct product name'
    def pac(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				hg=b[i+1]+' units'
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def pas(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				hg=b[i+3]+' units'
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def pcp(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				hg='₹'+b[i+2]
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def psp(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				hg='₹'+b[i+4]
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def pmi(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				hg='₹'+str(float(b[i+2])*int(b[i+1]))
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def pme(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				hg='₹'+str(float(b[i+4])*int(b[i+3]))
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def pbft(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				g=int(b[i+1])*float(b[i+2])
    				h=int(b[i+3])*float(b[i+4])
    				if h>g:
    					hg='₹'+str(h-g)
    				elif g>h:
    					hg='₹0.00'
    				elif g==h:
    					hg='Profit and loss are equal'
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def plos(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				g=int(b[i+1])*float(b[i+2])
    				h=int(b[i+3])*float(b[i+4])
    				if g>h:
    					hg='₹'+str(g-h)
    				elif h>g:
    					hg='₹0.00'
    				elif g==h:
    					hg='Profit and loss are equal'
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def pamlft(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		hg=pnm
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg=''
    			elif b[i]==pnm:
    				g=int(b[i+1])
    				h=int(b[i+3])
    				if g>h:
    					hg=str(g-h)+' units'
    				elif h>g:
    					hg='Error'
    				elif g==h:
    					hg='0 units'
    			elif pnm not in b:
    				hg=''
    		return hg
    	except Exception as e:
    		return ''
    def updateas(self,nup,v):
    	try:
    		if (len(v)>0 and int(v)>0) :
    			fo=1
    	except:
    		shol_popup('Kindly give the amount correctly.')
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		c=0
    		fui=0
    		y=1
    		if len(nup)==0:
    			shol_popup('Kindly give the'+'\n'+' product name.')
    			y=0
    		if nup not in b and len(nup)>0:
    			shol_popup('Kindly give the'+'\n'+' product name correctly.')
    			fui=1
    		for i in range (len(b)):
    			if b[i]==nup:
    				b[i+3]=str(int(b[i+3])+int(v))
    		gh=' '.join(b)
    		f=open('AppCS/data.txt','w')
    		f.write(gh)
    		f.close()
    		if fo==1 and fui !=1 and len(nup)>0:
    			show_popup()
    	except:
    		pass
    def excelll(self):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		todays_date = 'Data statsistics '+str(datetime.now().strftime("%Y-%m-%d %H:%M") )+ '.xlsx'
    		w = xlsxwriter.Workbook(todays_date)
    		ws=w.add_worksheet()
    		bold = w.add_format({'bold': True})
    		money = w.add_format({'num_format': '₹##,##,##,###.##0'})
    		r=c=0
    		ws.write(r,c,'Product',bold)
    		ws.write(r,c+1,'Amt. Bought',bold)
    		ws.write(r,c+2,'Cost Price',bold)
    		ws.write(r,c+3,'Amt. Sold',bold)
    		ws.write(r,c+4,'Selling Price',bold)
    		ws.write(r,c+5,'Loss',bold)
    		ws.write(r,c+6,'Profit',bold)
    		ws.write(r,c+7,'Money Invested',bold)
    		ws.write(r,c+8,'Money Earned',bold)
    		ws.write(r,c+9,'Amt. Left',bold)
    		r=1
    		for i in range(1,len(b)-1,5):
    			g=float(b[i+1])*float(b[i+2])
    			h=float(b[i+3])*float(b[i+4])
    			hgf=int(b[i+3])
    			gf=int(b[i+1])
    			if gf>hgf:
    				aml=gf-hgf
    			elif hgf==gf:
    				aml=hgf-gf
    			elif hgf>gf:
    				aml='Wrong input'
    			if g>h:
    				loss=g-h
    				profit=0
    			elif h>g:
    				loss=0
    				profit=h-g
    			elif h==g:
    				loss=profit=h-g
    			cp=float(b[i+2])
    			sp=float(b[i+4])
    			ws.write(r,c,b[i])
    			ws.write(r,c+1,b[i+1])
    			ws.write(r,c+2,cp,money)
    			ws.write(r,c+3,b[i+3])
    			ws.write(r,c+4,sp,money)
    			ws.write(r,c+5,loss,money)
    			ws.write(r,c+6,profit,money)
    			ws.write(r,c+7,g,money)
    			ws.write(r,c+8,h,money)
    			ws.write(r,c+9,aml)
    			r+=1
    		w.close()
    		sho_popup()
    	except Exception as e:
    		r=str(e)
    		shol_popup( 'Some error. '+r)
    def benefit(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg='Please enter Product name '
    			elif b[i]==pnm:
    				g=float(b[i+1])*float(b[i+2])
    				h=float(b[i+3])*float(b[i+4])
    				if g>h:
    					y=g-h
    					r=str(y)
    					hg='You still need to recover '+r+'\n'+'Keeping going You will recover it soon. :)'
    				elif h>g:
    					y=h-g
    					r=str(y)
    					hg='Your curent benefit from the product is '+r+'\n'+'Congrats ;)'
    				elif h==g:
    					hg='Your loss and gain stats from the product are equal.'
    			elif len(pnm)>0 and pnm not in b:
    				hg='Please enter valid product name.'
    		return hg
    	except Exception as e:
    		return 'Some error. Please enter valid product name.'
    def mi(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		c=0
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg='Enter the product name.'
    			elif b[i]==pnm:
    				g=float(b[i+1])*float(b[i+2])
    				y=str(g)
    				hg='Money Invested by you in the product is '+y+'\n'+'Hope you recover it soon.' +'\n'+'Have a Good Day :)'
    			elif pnm not in b:
    				hg='Enter valid Product name.'
    		return hg
    	except Exception as e:
    		return 'Some error. Please enter product name correctly.'
    def amt(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		c=0
    		for i in range (len(b)):
    			if len(pnm)==0:
    				hg='Please enter product name.'
    			elif b[i]==pnm:
    				g=str(b[i+1])
    				hg= 'The quantity of product you bought is '+g
    			elif pnm not in b:
    				hg='Enter valid product name.'
    		return hg
    	except Exception as e:
    		return 'Some error. Please put the product name correctly.'
    def me(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		c=0
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg='Please enter product name.'
    			elif b[i]==pnm:
    				g=float(b[i+3])*float(b[i+4])
    				y=str(g)
    				hg='Money Earned from the product is '+y+'\n'+'Hurray!!! ;)'
    			elif pnm not in b:
    				hg='Enter valid product name.'
    		return hg
    	except Exception as e:
    		return 'Some error. Please put the product name correctly.'
    def sp(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		c=0
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg='Please enter product name.'
    			elif b[i]==pnm:
    				g=str(b[i+4])
    				hg='Selling price of the product is '+g
    			elif pnm not in b:
    				hg='Enter valid product name.'
    		return hg
    	except Exception as e:
    		return 'Some error. Please put the product name correctly.'
    def cp(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		c=0
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg='Please enter product name.'
    			elif b[i]==pnm:
    				g=str(b[i+2])
    				hg='Cost price of the product is '+g
    			elif pnm not in b:
    				hg='Enter valid product name.'
    		return hg
    	except Exception as e:
    		return 'Some error. Please put the product name correctly.'
    def amts(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		c=0
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg='Please enter product name.'
    			elif b[i]==pnm:
    				g=str(b[i+3])
    				hg='You sold '+g+' units.'
    			elif pnm not in b:
    				hg='Enter valid product name.'
    		return hg
    	except Exception as e:
    		return 'Some error. Please put the product name correctly.'
    def amtsleft(self,pnm):
    	try:
    		f=open('AppCS/data.txt','r')
    		t=f.read()
    		b=t.split()
    		c=0
    		for i in range(len(b)):
    			if len(pnm)==0:
    				hg='Please enter product name.'
    			elif b[i]==pnm:
    				if int(b[i+1])>int(b[i+3]):
    					g=str(int(b[i+1])-int(b[i+3]))
    					hg='You are left with '+g+' units.'
    				elif int(b[i+1])<int(b[i+3]):
    					g=str(int(b[i+3])-int(b[i+1]))
    					hg='You are left with -'+g+' units.'
    				elif int(b[i+1])==int(b[i+3]):
    					g=str(int(b[i+1])-int(b[i+2]))
    					hg="You don't have any unit of this product."
    			elif pnm not in b:
    				hg='Enter valid product name.'
    		return hg
    	except Exception as e:
    		return 'Some error. Please put the product name correctly.'
class Infoline(BoxLayout):
    pass
class Add_new_product(Screen):
    pass
class Updatepd(Screen):
	def updatenm(self,nup,v):
	   try:
	   	f=open('AppCS/data.txt','r')
	   	t=f.read()
	   	b=t.split()
	   	c=0
	   	fui=0
	   	y=1
	   	if len(nup)==0:
	   		shol_popup('Kindly give the'+'\n'+' product name.')
	   		y=0
	   	elif len(v)==0:
	   		shol_popup('Kindly give the'+'\n'+' new product name.')
	   	elif nup not in b and len(nup)>0:
	   		shol_popup('Kindly give the existing'+'\n'+'product name correctly.')
	   		fui=1
	   	if len(nup)>0 and len(v)>0 and nup in b:
	   		for i in range (len(b)):
	   			if b[i]==nup:
	   				b[i]=v
	   				show_popup()
	   	gh=' '.join(b)
	   	f=open('AppCS/data.txt','w')
	   	f.write(gh)
	   	f.close()
	   except:
	   	fu=0
	def updateac(self,nup,v):
	   try:
	   	if (len(v)>0 and int(v)>0) :
	   		fo=1
	   except:
	   	shol_popup('Kindly give the amount correctly.')
	   try:
	    	f=open('AppCS/data.txt','r')
	    	t=f.read()
	    	b=t.split()
	    	c=0
	    	fui=0
	    	y=1
	    	if len(nup)==0:
	    		shol_popup('Kindly give the'+'\n'+' product name.')
	    	elif len(v)==0:
	    		shol_popup('Kindly give the'+'\n'+'amount.')
	    	elif nup not in b and len(nup)>0:
	    		shol_popup('Kindly give the'+'\n'+' product name correctly.')
	    		fui=1
	    	for i in range (len(b)):
	    		if b[i]==nup:
	    			b[i+1]=str(int(b[i+1])+int(v))
	    	gh=' '.join(b)
	    	f=open('AppCS/data.txt','w')
	    	f.write(gh)
	    	f.close()
	    	if fo==1 and fui !=1 and len(nup)>0:
	    		show_popup()
	   except:
	    	pass
	def updatecp(self,nup,v):
	   try:
	   	if (len(v)>0 and float(v)>0) :
	   		fo=1
	   except:
	   	shol_popup('Kindly give the cost correctly.')
	   try:
	   	f=open('AppCS/data.txt','r')
	   	t=f.read()
	   	b=t.split()
	   	c=0
	   	fui=0
	   	y=1
	   	if len(nup)==0:
	   		shol_popup('Kindly give the'+'\n'+' product name.')
	   		y=0
	   	if nup not in b and len(nup)>0:
	   		shol_popup('Kindly give the'+'\n'+' product name correctly.')
	   		fui=1
	   	for i in range (len(b)):
	   		if b[i]==nup:
	   			b[i+2]=str(float(v))
	   	gh=' '.join(b)
	   	f=open('AppCS/data.txt','w')
	   	f.write(gh)
	   	f.close()
	   	if fo==1 and fui !=1 and len(nup)>0:
	   		show_popup()
	   except:
	   	pass
	def updateas(self,nup,v):
	   try:
	   	if (len(v)>0 and int(v)>0) :
	   		fo=1
	   except:
	   	shol_popup('Kindly give the amount correctly.')
	   try:
	   	f=open('AppCS/data.txt','r')
	   	t=f.read()
	   	b=t.split()
	   	c=0
	   	fui=0
	   	y=1
	   	if len(nup)==0:
	   		shol_popup('Kindly give the'+'\n'+' product name.')
	   		y=0
	   	if nup not in b and len(nup)>0:
	   		shol_popup('Kindly give the'+'\n'+' product name correctly.')
	   		fui=1
	   	for i in range (len(b)):
	   		if b[i]==nup:
	   			b[i+3]=str(int(b[i+3])+int(v))
	   	gh=' '.join(b)
	   	f=open('AppCS/data.txt','w')
	   	f.write(gh)
	   	f.close()
	   	if fo==1 and fui !=1 and len(nup)>0:
	   		show_popup()
	   except:
	   	pass
	def updatesp(self,nup,v):
	   try:
	   	if (len(v)>0 and float(v)>0):
	   		fo=1
	   except:
	   	shol_popup('Kindly give the cost correctly.')
	   try:
	   	f=open('AppCS/data.txt','r')
	   	t=f.read()
	   	b=t.split()
	   	c=0
	   	fui=0
	   	y=1
	   	if len(nup)==0:
	   		shol_popup('Kindly give the'+'\n'+' product name.')
	   		y=0
	   	if nup not in b and len(nup)>0:
	   		shol_popup('Kindly give the'+'\n'+' product name correctly.')
	   		fui=1
	   	for i in range (len(b)):
	   		if b[i]==nup:
	   			b[i+4]=str(float(v))
	   	gh=' '.join(b)
	   	f=open('AppCS/data.txt','w')
	   	f.write(gh)
	   	f.close()
	   	if fo==1 and fui !=1 and len(nup)>0:
	   		show_popup()
	   except:
	   	pass
class Popups(FloatLayout):
	pass
class Popus(FloatLayout):
	pass
class InfoLline(BoxLayout):
    pass
class Bftc(Screen):
	pass
class Bftrslt(Screen):
	pass
class Merslt(Screen):
	pass
class Mirslt(Screen):
	pass
class Amtrslt(Screen):
	pass
class Amtsrslt(Screen):
	pass
class Amtsleft(Screen):
	pass
class Sellingp(Screen):
	pass
class Costp(Screen):
	pass
class TestApp(App):
    try:
    	#by default rgstr file is written(1)to avoid it this is done.
    	f=open('AppCS/rgstir.txt','r')
    	t=f.read()
    	b=len(t)
    	f.close()
    	c=0
    	for i in range(b):
    		if t[i].isalpha()==False:
    			c+=1
    	if c==b:
    		f=1
    	if f==1:
    	    def build(self):
    	    	sm = ScreenManager()
    	    	sm.add_widget(Signin(name='sg'))
    	    	sm.add_widget(Register(name='rg'))
    	    	sm.add_widget(MenuScreen(name='menu'))
    	    	sm.add_widget(Add_new_product(name='add_staff'))
    	    	sm.add_widget(Updatepd(name='updatec'))
    	    	sm.add_widget(Bftc(name='bftc'))
    	    	sm.add_widget(Bftrslt(name='bftr'))
    	    	sm.add_widget(Merslt(name='mer'))
    	    	sm.add_widget(Mirslt(name='mir'))
    	    	sm.add_widget(Amtrslt(name='amtr'))
    	    	sm.add_widget(Amtsrslt(name='amtsr'))
    	    	sm.add_widget(Amtsleft(name='amtsleft'))
    	    	sm.add_widget(Sellingp(name='selp'))
    	    	sm.add_widget(Costp(name='cop'))
    	    	f=open('AppCS/rgstir.txt','w')
    	    	f.write('1')
    	    	f.close()
    	    	return sm
    	elif b>1:
    	    def build(self):
    	    	sm = ScreenManager()
    	    	sm.add_widget(MenuScreen(name='menu'))
    	    	sm.add_widget(Add_new_product(name='add_staff'))
    	    	sm.add_widget(Updatepd(name='updatec'))
    	    	sm.add_widget(Bftc(name='bftc'))
    	    	sm.add_widget(Bftrslt(name='bftr'))
    	    	sm.add_widget(Merslt(name='mer'))
    	    	sm.add_widget(Mirslt(name='mir'))
    	    	sm.add_widget(Amtrslt(name='amtr'))
    	    	sm.add_widget(Amtsrslt(name='amtsr'))
    	    	sm.add_widget(Amtsleft(name='amtsleft'))
    	    	sm.add_widget(Sellingp(name='selp'))
    	    	sm.add_widget(Costp(name='cop'))
    	    	
    	    	return sm
    except Exception as e:
        def build(self):
        	sm = ScreenManager()
        	sm.add_widget(Signin(name='sg'))
        	sm.add_widget(Register(name='rg'))
        	sm.add_widget(MenuScreen(name='menu'))
        	sm.add_widget(Add_new_product(name='add_staff'))
        	sm.add_widget(Updatepd(name='updatec'))
        	sm.add_widget(Bftc(name='bftc'))
        	sm.add_widget(Bftrslt(name='bftr'))
        	sm.add_widget(Merslt(name='mer'))
        	sm.add_widget(Mirslt(name='mir'))
        	sm.add_widget(Amtrslt(name='amtr'))
        	sm.add_widget(Amtsrslt(name='amtsr'))
        	sm.add_widget(Amtsleft(name='amtsleft'))
        	sm.add_widget(Sellingp(name='selp'))
        	sm.add_widget(Costp(name='cop'))
        	path = "AppCS/Go On"
        	access_rights = 0o755
        	try:
        		os.makedirs(path, access_rights)
        	except OSError:
        		print('Error')
        	f=open('AppCS/rgstir.txt','w')
        	f.write('1')
        	f.close()
        	f=open('AppCS/data.txt','w')
        	f.write('1')
        	f.close()
        	return sm
    def rgstr(self,nm,pas,unm):
    	f=open('AppCS/rgstir.txt','a')
    	f.write(nm+' '+unm+' '+pas)
    	f.close()
    def save(self, namei,amt,cp,amts,sp):
	    fob=open('AppCS/data.txt','a')
	    fob.write('\n')
	    fob.write(namei + ' '+amt+ ' '+cp+ ' '+amts+ ' '+sp)
	    fob.close()
    
    def logunm(self,unm):
    	f=open('AppCS/rgstir.txt','r')
    	t=f.read()
    	b=t.split()
    	for i in range(len(b)):
    		if unm==b[i]:
    			s=str(b[i])
    		elif b[i]!=unm:
    			s='ulula'
    	return s
    def logpas(self,unm,pas):
    	f=open('AppCS/rgstir.txt','r')
    	t=f.read()
    	b=t.split()
    	for i in range(len(b)):
    		if unm==b[i]:
    			if b[i-1].isalpha():
    				if b[i+1]==pas:
    					s=str(b[i+1])
    		elif b[i]!=unm:
    			s='ulula'
    	return s
    def excell(self):
    	todays_date = 'Data '+str(datetime.now().strftime("%Y-%m-%d %H:%M") )+ '.xlsx'
    	w = xlsxwriter.Workbook(todays_date)
    	ws=w.add_worksheet()
    	bold = w.add_format({'bold': True})
    	money = w.add_format({'num_format': '₹##,##,##,###.##0'})
    	f=open('AppCS/data.txt','r')
    	g=f.read()
    	b=g.split()
    	r=c=0
    	ws.write(r,c,'Product',bold)
    	ws.write(r,c+1,'Amt.Bought',bold)
    	ws.write(r,c+2,'Cost Price',bold)
    	ws.write(r,c+3,'Amt.Sold',bold)
    	ws.write(r,c+4,'Selling Price',bold)
    	r=1
    	c=0
    	for i in range(1,len(b)-1,5):
    		cp=float(b[i+2])
    		sp=float(b[i+4])
    		ws.write(r,c,b[i])
    		ws.write(r,c+1,b[i+1])
    		ws.write(r,c+2,cp,money)
    		ws.write(r,c+3,b[i+3])
    		ws.write(r,c+4,sp,money)
    		r+=1
    	w.close()
    	sho_popup()
				
def show_popup(): 
    show = Popups()
    popupWindow = Popup(title ="Notification", content = show, size_hint =(None, None), size =(400, 250))
    popupWindow.open()
def sho_popup(): 
    show = Popus()
    popupWindow = Popup(title ="Successfully Generated", content = show, size_hint =(None, None), size =(400, 200))
    popupWindow.open()
def shol_popup(y):
    popupWindow = Popup(title ="Error Occured", content = Label(text=y), size_hint =(None, None), size =(400, 200))
    popupWindow.open()
    
t=TestApp()
t.run()