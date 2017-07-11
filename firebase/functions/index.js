const functions = require('firebase-functions');
const admin = require('firebase-admin');
const request = require('request-promise');
const buildUrl = require('build-url');

const language = require('@google-cloud/language')({apiVersion: 'v1beta2'});
const bigquery = require('@google-cloud/bigquery')();

admin.initializeApp(functions.config().firebase);


exports.notifyChannel = functions.database.ref('/news/{what}/{uid}')
  .onCreate(event => {
    const content = event.data.val().content;
    const config = functions.config().telegram;
    const url = buildUrl('https://api.telegram.org', {
      path: `bot${config.bot.token}/sendMessage`,
      queryParams: {
        chat_id: config.channel.chat_id,
      }
    });

    return Promise.all([language.document({content: content}).annotate()
      .then((results) => {
        const dataset = bigquery.dataset(functions.config().bigquery.datasetname);
        const table = dataset.table(functions.config().bigquery.tablename);

        const result = results[1];
        console.log(JSON.stringify(result.entities))
        return table.insert({
          ID: event.data.key,
          ENTITIES: result.entities,
          TIMESTAMP: new Date().getTime()
        });
      }).catch((error) => {
        throw error
      }),

      request({
        method: 'POST',
        uri: url,
        resolveWithFullResponse: true,
        body: {
          text: content
        },
        json: true
      }).then(response => {
        if (response.statusCode === 200) {
          return response.body.id;
        }
        throw response.body;
      })
    ]);
  }
);
