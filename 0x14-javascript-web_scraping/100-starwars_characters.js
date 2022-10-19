#!/usr/bin/node
const request = require('request');

const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  for (const character of JSON.parse(body).characters) {
    request(character, function (error, response, body) {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
