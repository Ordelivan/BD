from server.routers import user, personal, genre, ticket, performance

routers = (user.router, personal.router, genre.router,ticket.router,performance.router)
