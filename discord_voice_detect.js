const Discord = require('discord.js');
const client = new Discord.Client({ ws: { intents: ['GUILDS', 'GUILD_MESSAGES', 'GUILD_MEMBERS', 'GUILD_VOICE_STATES'] } });

//Hyper
var net = require('net');
var c_client = new net.Socket();
var c_speaking_status = false;


//connect to a local server initiated with python
c_client.connect(1338, '127.0.0.1', function() {
	console.log('Connected');
});


function getRandomInt() {
  return Math.round(Math.random() * 100);
}


client.on('ready', () => {
	console.log(`Logged in as ${client.user.tag}!`);
});

//Roller
client.on('message', message => {
	if (message.content === '!roll') {
		message.channel.send(message.author.username + "'s result: " + getRandomInt().toString());
	}
});

client.on('message', async message => {
	// Join the same voice channel of the author of the message
	if (message.content === 'Command: join_my_channel') {
		const vc = message.client.channels.cache.get("")//Input the channel ID here
		vc.join()
	}
});

client.on("guildMemberSpeaking", function(member, speaking){
    //console.log('a guild member starts/stops speaking: ' + member.displayName);
    if (member.displayName == "name_of_the_member"){ //Input the name of the member here that you want to detect
    	c_speaking_status = !c_speaking_status;
    	c_client.write(c_speaking_status.toString());
    }
});

//Input the login key here
client.login('');
