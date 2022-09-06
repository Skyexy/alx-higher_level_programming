#!/usr/bin/node
if (process.argv.length < 2)
{
	console.log('No argument');
}
else if (process.argv.length === 2)
{
	console.log(process.argv.length);
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
