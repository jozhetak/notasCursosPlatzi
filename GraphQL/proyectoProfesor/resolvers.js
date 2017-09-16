const Curso = require('./models/Curso')
const Profesor = require('./models/Profesor')

const resolvers = {
  Query: {
    cursos: () => Curso.query().eager('[profesor, comentarios]'),
    profesores: () => Profesor.query().eager('cursos'),
    curso: (rootValue, args) => Curso.query().eager('[profesor, comentarios]').findById(args.id),
    profesor: (rootValue, args) => Profesor.query().eager('cursos').findById(args.id),
    buscar: (_, args) => {
      return [
        Profesor.query().findById(3),
        Curso.query().findById(1)
      ]
    }
  },
  ResultadoBusqueda: {
    __resolveType: (obj) => {
      if (obj.nombre) return 'Profesor'
      return 'Curso'
    }
  },
  Mutation: {
    profesorAdd: (_, args) => {
      return Profesor.query().insert(args.profesor)
    },
    profesorEdit: (_, args) => {
      return Profesor.query().patchAndFetchById(args.profesorId, args.profesor)
    },
    profesorDelete: (_, args) => {
      return Profesor.query().findById(args.profesorId).then((profesor) => {
        return Profesor.query().deleteById(args.profesorId).then((filasBorradas) => {
          if (filasBorradas > 0) return profesor
          throw new Error(`El profesor con id ${args.profesorId} no se pudo eliminar`)
        })
      })
    }
  }
}

module.exports = resolvers
