#from os import truncate
from flask import Flask, request
from pymessenger import Bot
#import json
app = Flask(__name__)

ACCESS_TOKEN = "EAASTt2bmmp4BADzUyyT4uD4qS7U954KmVrixE5pQrzr7Dp3Y2bcTppawLOEIISXY10n5Km71tPI9VehwWtke1ZCy6ZCtGoV2ohZAdLhMlwNe3K6nd1FaIPKwH5rPZAnD2gT2BbOgmyJJbO0ZCwaqP9zspuZBgkA2Ot1SslQMkDZBh4QNM92wjx4"
bot = Bot(ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"
qr=[
      {
        "content_type":"text",
        "title":"About Us",
        "payload":"try text"
        
      },{
        "content_type":"text",
        "title":"Contact Us",
        "payload":"try text"
    
      },{
        "content_type":"text",
        "title":"Options",
        "payload":"try text"
    
      },{
        "content_type":"text",
        "title":"Our Projects",
        "payload":"try text"
    
      },{
        "content_type":"text",
        "title":"Webpage",
        "payload":"try text"
    
      }
      
    ]
  
Contact=[
      {
        "content_type":"text",
        "title":"E-mail",
        "payload":"try text"
        
      },{
        "content_type":"text",
        "title":"Mobile",
        "payload":"try text"
    
      },{
        "content_type":"text",
        "title":"Phone",
        "payload":"try text"
    
      },{
        "content_type":"text",
        "title":"Facebook",
        "payload":"try text"
    
      },{
        "content_type":"text",
        "title":"Location",
        "payload":"try text"
    
      }
      
    ]



but=[{
                        "title": "Asylex",
                        "subtitle": "free online legal aid on Swiss asylum law",
                        "item_url": "https://asylex.ch/",               
                        "image_url": "https://media-exp2.licdn.com/mpr/mpr/shrink_200_200/AAEAAQAAAAAAAAr8AAAAJDYyNGU1NWM4LTA4NzYtNGU4Yy1hNmY5LTA3MDAzOWRhZWFkNQ.png",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://asylex.ch/docs/faq_en.pdf",
                            "title": "Open FAQ"
                        }, {
                            "type": "postback",
                            "title": "Call Postback",
                            "payload": "try"
                            

                            
                        }],
                    }, {
                        "title": "Google",
                        "subtitle": "Find all your answers",
                        "item_url": "https://www.google.com/",               
                        "image_url": "https://www.google.ch/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://www.google.ch/",
                            "title": "Google Suche"
                        }, {
                            "type": "postback",
                            "title": "Call Postback",
                            "payload":"try"
                        },
                        {
                            "type":"phone_number",
                            "title":"01752931371",
                            "payload":"+8801752931371"
                            }]
                    }]

about=[{
                        "title": "Our Web page",
                        "subtitle": "This is our 1st webpage",
                        "item_url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/?fbclid=IwAR1mew2GnFmzf32_VWeXUQwAQt0eeiZMSweBKoGeCd33xoc4dCYpHCp_NFI#about",               
                        "image_url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/assets/images/slide-02.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/?fbclid=IwAR1mew2GnFmzf32_VWeXUQwAQt0eeiZMSweBKoGeCd33xoc4dCYpHCp_NFI#about",
                            "title": "About Us"
                        }],
                    }, {
                        "title": "Dagency",
                        "subtitle": "2nd website",
                        "item_url": "https://dagency2.herokuapp.com/contact",               
                        "image_url": "http://bmgmarketing.co.za/wp-content/uploads/2014/10/websites1.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://dagency2.herokuapp.com/contact",
                            "title": "About Us"
                        }]
                    }]

webp=[{
                        "title": "Our Web page",
                        "subtitle": "This is our 1st webpage",
                        "item_url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/?fbclid=IwAR1mew2GnFmzf32_VWeXUQwAQt0eeiZMSweBKoGeCd33xoc4dCYpHCp_NFI",               
                        "image_url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/assets/images/slide-02.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/?fbclid=IwAR1mew2GnFmzf32_VWeXUQwAQt0eeiZMSweBKoGeCd33xoc4dCYpHCp_NFI",
                            "title": "Url"
                        }],
                    }, {
                        "title": "Dagency",
                        "subtitle": "2nd website",
                        "item_url": "https://dagency2.herokuapp.com/",               
                        "image_url": "http://bmgmarketing.co.za/wp-content/uploads/2014/10/websites1.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://dagency2.herokuapp.com/",
                            "title": "Url"
                        }]
                    }]


works=[{
                        "title": "Our projects",
                        "subtitle": "the projects that we delivered ",
                        "item_url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/?fbclid=IwAR1mew2GnFmzf32_VWeXUQwAQt0eeiZMSweBKoGeCd33xoc4dCYpHCp_NFI#projects",               
                        "image_url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/assets/images/project-big-item-05.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/?fbclid=IwAR1mew2GnFmzf32_VWeXUQwAQt0eeiZMSweBKoGeCd33xoc4dCYpHCp_NFI#projects",
                            "title": "Projects"
                        }]
                        }]

opt=[{
                        "title": "Web Design",
                        "subtitle": "",
                        "item_url": "https://dagency2.herokuapp.com/Product",               
                        "image_url": "http://erothtechnologies.com/assets/uploads/file-59.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://dagency2.herokuapp.com/Product",
                            "title": "Web Design"
                        }],
                    }, {
                        "title": "Web Development",
                        "subtitle": "",
                        "item_url": "https://dagency2.herokuapp.com/Product1",               
                        "image_url": "https://dagency2.herokuapp.com/Product1",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://dagency2.herokuapp.com/Product1",
                            "title": "Web Development"
                        }]
                    },
                    {
                        "title": "Chat Bots",
                        "subtitle": "",
                        "item_url": "https://dagency2.herokuapp.com/Product2",               
                        "image_url": "https://dagency2.herokuapp.com/Product2",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://dagency2.herokuapp.com/Product2",
                            "title": "Chat Bots"
                        }]
                    },
                    {
                        "title": "Others",
                        "subtitle": "",
                        "item_url": "https://dagency2.herokuapp.com/Product3",               
                        "image_url": "https://utemplates.net/wp-content/uploads/2016/10/utemplates_rage-digital-agency-psd-template-freebie-i2.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://dagency2.herokuapp.com/Product3",
                            "title": "Ohters"
                        }]
                    }]

fb=[{
                        "title": "Facebook Profile",
                        "subtitle": "Contact me on.",
                        "item_url": "https://www.facebook.com/profile.php?id=100011547033268",               
                        "image_url": "https://scontent.fdac75-1.fna.fbcdn.net/v/t1.6435-1/s200x200/175535655_1278763382518551_5965458414599422879_n.jpg?_nc_cat=108&ccb=1-3&_nc_sid=7206a8&_nc_eui2=AeGpcjn4QqEWXlk-JrA6LwOIts564uvBWW22znri68FZbfkI9aa5E7PM7yplVOdeAm934o_ONeGEChhEPglN4KVi&_nc_ohc=xG1bq4nbk2oAX8dmuiS&_nc_ht=scontent.fdac75-1.fna&tp=7&oh=e0777d6907b5a511ba72246a973d9f71&oe=60DD51FD",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://www.facebook.com/profile.php?id=100011547033268",
                            "title": "Fb Pro"
                        }]
                        }]


contk=[{
                        "title": "Our Web page",
                        "subtitle": "This is our 1st webpage",
                        "item_url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/?fbclid=IwAR3-5ZZZnVlmaa7Ooystm5ERpavJvbIcKnzS3FlmR_0NE5SsCwTj4a9NZD4#contact-us",               
                        "image_url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/assets/images/slide-02.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://zhmvfhrznfw50orobpeo5w-on.drv.tw/EXCOMRADE/?fbclid=IwAR3-5ZZZnVlmaa7Ooystm5ERpavJvbIcKnzS3FlmR_0NE5SsCwTj4a9NZD4#contact-us",
                            "title": "Contact"
                        }],
                    }, {
                        "title": "Dagency",
                        "subtitle": "2nd website",
                        "item_url": "https://dagency2.herokuapp.com/contact",               
                        "image_url": "http://bmgmarketing.co.za/wp-content/uploads/2014/10/websites1.jpg",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://dagency2.herokuapp.com/contact",
                            "title": "Contact"
                        }]
                    }]

gp=[
                {
                    "content_type":"text",
                    "title":"Logo Design",
                    "payload":"try text"
                    
                },{
                    "content_type":"text",
                    "title":"Typhography",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Mug Design",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Card Design",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Shart Design",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Bannar Design",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"back",
                    "payload":"try text"
                
                }
                
                ]
b=[{"content_type":"text",
                "title":"back",
                "payload":"try text"
                },{
                "content_type":"text",
                "title":"Contact Us",
                "payload":"try text"
                },{"content_type":"text",
                "title":"Digital Marketing",
                "payload":"try text"
                },{
                "content_type":"text",
                "title":"Graphic Design",
                "payload":"try text"
                },{"content_type":"text",
                "title":"Video Editing",
                "payload":"try text"
                },{
                "content_type":"text",
                "title":"Animation",
                "payload":"try text"
                },{"content_type":"text",
                "title":"Professional Photography",
                "payload":"try text"
                },{
                "content_type":"text",
                "title":"Wedding Zone",
                "payload":"try text"
                },{"content_type":"text",
                "title":"IT Support",
                "payload":"try text"
                }]
an=[
                {
                    "content_type":"text",
                    "title":"Cartoon Animation",
                    "payload":"try text"
                    
                },{
                    "content_type":"text",
                    "title":"Video Intro",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"PowerPoint Animation",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Scripting Animation",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Cartoon Design",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Gaming Animation",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"back",
                    "payload":"try text"
                
                }
                
                ]

pp=[
                {
                    "content_type":"text",
                    "title":"Wedding Photography",
                    "payload":"try text"
                    
                },{
                    "content_type":"text",
                    "title":"Natural Photography",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Concept Photography",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"Business Photography",
                    "payload":"try text"
                
                },{
                    "content_type":"text",
                    "title":"back",
                    "payload":"try text"
                
                }
                
]


def wc(s,query):
       
        
        welcmoe=['Hi','Hlw','hello','Hello','hlw','hi','Get Started']
        bye=['Bye','Good Bye','bye','good bye','see u','See you','Bye there','bye there']
        if query in welcmoe:
            bot.send_quick_replies_message(s,"U are MOst WeLcome to OUr group. how can I help U sir?",qr)
                   
        
        #if query in welcmoe:
                #bot.send_generic_message(s,but)
                #bot.send_quick_replies_message(s,"Welcome To Our Page",qro)
        elif query =="About Us":
            bot.send_generic_message(s,about)
            bot.send_quick_replies_message(s,"Welcome To Our Page",b)
        

        elif query =="Webpage":
            bot.send_generic_message(s,webp)
            bot.send_quick_replies_message(s,"Sir We have 2 web pages.. one for take order and one for our information",qr)
        elif query == "our works":
            bot.send_generic_message(s,works)
        elif query =="Contact Us":
            bot.send_generic_message(s,contk)

        elif query =="Our Projects":
            bot.send_generic_message(s,works)
        elif query =="Chat With Me":
            bot.send_text_message(s,"Sir I am Busy Right now... Sir u can Call Me on -- 01752931371")
        elif query =="Options":
            
                msg ='''
                Digital Marketing
                Graphic Design
                Video Editing
                Animation
                Professional Photography
                Wedding Zone
                IT Support
                '''
                bot.send_generic_message(s,opt)
                bot.send_quick_replies_message(s,"Welcome To Our Page",b)
        elif query in bye:
                bot.send_text_message(s,'Bye Sir.....\n Have a nice day')
        elif query =='back':
                bot.send_quick_replies_message(s,"We are backing sir.",qr)
        elif query =='Mobile':
                bot.send_text_message(s,"0175293171")
        elif query =='E-mail':
                bot.send_text_message(s,'mainkchandrabiswas72@gmail.com')

        elif query =='Phone':
                bot.send_text_message(s,'nai')
        elif query == 'Facebook':
                bot.send_generic_message(s,fb)
        elif query =="Digital Marketing":
            bot.send_quick_replies_message(s,"U can contact us on below options",Contact)
        elif query =="Graphic Design":

            bot.send_quick_replies_message(s,"sir We have some profetional designers... they will design ur dream as real... sir what kind or design do u want... our opthons below",gp)
        elif query =="Wedding Zone":
            bot.send_quick_replies_message(s,"its a part of our life... and it is one of the most beautiful moment in one's life. to make the day more memoriable we will help you we will make tha day more glorious for your next life",Contact)
        elif query =="Animation":
            bot.send_quick_replies_message(s,"Sir We are here to give life to your imagenation ",an)
        elif query =="IT Support":
            bot.send_quick_replies_message(s,"sorry for that. this bot is undr constraction. you can find us on mail or phone number or you can direct meet on our shop.. have a nice day",Contact)
        elif query =="Video Editing":
            bot.send_quick_replies_message(s,"sorry for that. this bot is undr constraction. you can find us on mail or phone number or you can direct meet on our shop.. have a nice day",Contact)
        elif query =="Professional Photography":
            bot.send_quick_replies_message(s,"Capture the moment of life... and save it. Sir We will provide with u all the enjoy abale moment of the day.",pp)
        elif query =="Logo Design" or query == "Card Design":
            bot.send_text_message(s,'A Logo or A Card  is not just logo or card. \n It is the sign of your choice and your test. It represent your business and your personality.')
        elif query =="Bannar Design" or query=='Mug Design':
            bot.send_text_message(s,'Design what you prefer, design mug with your picture or your favorite design or senary.\n\n more creative bannar more your publish.')
            
        elif query =="Cartoon Animation" or query=="Scripting Animation":
            bot.send_text_message(s,'contact me for more information')
        elif query =="Cartoon Design" or query=="PowerPoint Animation":
            bot.send_quick_replies_message(s,"sorry for that. this bot is undr constraction. you can find us on mail or phone number or you can direct meet on our shop.. have a nice day",Contact)
        elif query =="Natural Photography" or query=='Concept Photography':
            bot.send_quick_replies_message(s,"sorry for that. this bot is undr constraction. you can find us on mail or phone number or you can direct meet on our shop.. have a nice day",Contact)
        elif query =="Wedding Photography":
            bot.send_quick_replies_message(s,"sorry for that. this bot is undr constraction. you can find us on mail or phone number or you can direct meet on our shop.. have a nice day",Contact)
        elif query =="Business Photohygrap":
            bot.send_quick_replies_message(s,"sorry for that. this bot is undr constraction. you can find us on mail or phone number or you can direct meet on our shop.. have a nice day",Contact)
        
        
        '''else:
                bot.send_text_message(s, query)'''
        if query =="h5":
            
                bot.send_generic_message(s,but)
                bot.send_quick_replies_message(s,"Welcome To Our Page",but)
@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
        
	#print(request.data)
	data = request.get_json(force=True,silent=False); #print(request.get_json(force=True,silent=True))
    
	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:

				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# HANDLE NORMAL MESSAGES HERE
					if messaging_event['message'].get('text'):
						# HANDLE TEXT MESSAGES
						query = messaging_event['message']['text']
						wc(sender_id,query);print(query)
						

	return "ok", 200

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=80,debug=True)


