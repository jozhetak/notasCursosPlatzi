const express = require('express')
const bodyParser = require('body-parser')
// Las llaves significan que sólo se importará esa función
const {graphqlExpress, graphiqlExpress} = require ('graphql-server-express')
const app = express()
const schema = require('./schema')
app.use(
  '/graphql',
  bodyParser.json(),
  graphqlExpress({schema})
)

app.use(
  '/graphiql', // En qué endpintURL
  graphiqlExpress({
    endpointURL: '/graphql'
  })
)

const PORT = 5678

// Escuhar el puerto y una función
// cuando responda
app.listen(PORT, () => {
  console.log('Servidor corriendo OK')
})
