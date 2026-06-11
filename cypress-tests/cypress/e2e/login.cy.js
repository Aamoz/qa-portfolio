describe('Login Tests', () => {
  it('should login successfully with valid credentials', () => {
    cy.visit('https://the-internet.herokuapp.com/login')
    cy.get('#username').type('tomsmith')
    cy.get('#password').type('SuperSecretPassword!')
    cy.get('button[type="submit"]').click()
    cy.get('.flash.success').should('contain', 'You logged into a secure area!')
  })

  it('should show error with invalid credentials', () => {
    cy.visit('https://the-internet.herokuapp.com/login')
    cy.get('#username').type('wronguser')
    cy.get('#password').type('wrongpassword')
    cy.get('button[type="submit"]').click()
    cy.get('.flash.error').should('contain', 'Your username is invalid!')
  })
})
