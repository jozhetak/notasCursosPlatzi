// Aquí estará el esquema de nuestra aplicacion
const {makeExecutableSchema, addMockFunctionsToSchema } = require('graphql-tools')
const casual = require ('casual')
const typeDefs = `
# Esto es un curso en el sistema
  type Curso{
    id: ID!
    titulo: String!
    # Esta es la descripcion del cuso
    descripcion: String!
    profesor: Profesor
    rating: Float @deprecated(reason: "Vamos a elminar este campo")
    comentarios: [Comentario]
  }

  type Profesor{
    id: ID!
    nombre: String!
    nacionalidad: String!
    genero: Genero
    cursos: [Curso]
  }

  type Comentario{
    id: ID!
    nombre: String!
    cuerpo: String!
  }

  enum Genero{
    MASCULINO
    FEMENINO
  }

  type Query{
    cursos: [Curso]
    profesores: [Profesor]
    curso(id: Int): Curso
    profesor(id: Int): Profesor
  }
`

const resolvers = {
  Query:{
    cursos: () => {
      return [{
        id: 1,
        titulo: 'Curso de GraphQL',
        descripcion: 'Aprendiendo GraphQL'
      },{
        id:2,
        titulo: 'Curso de JavaEE',
        descripcion: 'Aprendiendo Java'
      }]
    }
  },
  Curso: {
    profesor: () => {
      return {
        nombre: 'Pablo'
      }
    }
  },
  Profesores: () => {
    return [{

    }]
    }
  }
}

const schema = makeExecutableSchema({
  typeDefs,
  resolvers
})

addMockFunctionsToSchema({
  schema,
  mocks:{
    Curso: () =>{
      return{
        id:casual.uuid,
        titulo: casual.sentence,
        descripcion: casual.sentences(2)

      }
    },
    Profesor: () =>{
      return {
        id: casual.uuid,
        nombre: casual.name,
        nacionalidad: casual.country
      }
    }

  },
  preserveResolvers: false // Si es true priorizará los datos de resolvers
})



module.exports = schema
