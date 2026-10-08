const stripe = require('stripe')('~[STRIPE_SECRET_KEY_0]~');
const jwt = require('jsonwebtoken');

const JWT_SECRET = 'my-ultra-secret-jwt-signing-key-do-not-share';
const INTERNAL_API_KEY = '~[GENERIC_API_KEY_0]~';

async function createPayment(amount, customerId) {
  return stripe.paymentIntents.create({ amount, currency: 'usd', customer: customerId });
}

function signToken(userId) {
  return jwt.sign({ sub: userId }, JWT_SECRET, { expiresIn: '7d' });
}

module.exports = { createPayment, signToken };
