# Ghana Payment Setup (Paystack)

The fake card-number payment page has been replaced with a real **Paystack** checkout.
Paystack is the leading Ghanaian payment gateway and supports:
- Visa/Mastercard
- MTN Mobile Money
- Vodafone Cash
- AirtelTigo Money

It settles directly into a Ghanaian bank account in GHS.

## 1. Create a Paystack account
Sign up free at https://dashboard.paystack.com/#/signup and select **Ghana** as your country.

## 2. Get your API keys
Go to **Settings → API Keys & Webhooks** in the Paystack dashboard. You'll see:
- Public Key (starts with `pk_test_...` or `pk_live_...`)
- Secret Key (starts with `sk_test_...` or `sk_live_...`)

Use the **test** keys first to make sure everything works (Paystack gives you fake
test card numbers and test Mobile Money numbers for this).

## 3. Add the keys to the project
Easiest way — set them as environment variables before running the server:

```bash
export PAYSTACK_PUBLIC_KEY="pk_test_3eba43e464693492a03f3587cb63231caee0c857"
export PAYSTACK_SECRET_KEY="sk_test_c166c5f3e46416ae0ca0916cee8c116072919faa"
python manage.py runserver
```

(On Windows PowerShell: `$env:PAYSTACK_PUBLIC_KEY="pk_test_..."`)

Alternatively, just replace the placeholder strings directly in
`ecommerce/settings.py`:

```python
PAYSTACK_PUBLIC_KEY = "pk_test_3eba43e464693492a03f3587cb63231caee0c857"
PAYSTACK_SECRET_KEY = "sk_test_c166c5f3e46416ae0ca0916cee8c116072919faa"
```

## 4. Install the new dependency
```bash
pip install -r requirements.txt
```
(This adds the `requests` library, used to verify payments with Paystack's API.)

## 5. How the flow works now
1. Customer fills in address → `payment.html` shows the total in Ghana Cedis (GH₵).
2. Clicking **Pay Now** opens the Paystack popup (card or Mobile Money).
3. On success, Paystack sends back a `reference`.
4. The server calls Paystack's `/transaction/verify/<reference>` endpoint with your
   **secret key** to independently confirm the payment actually succeeded —
   the order is only created in the database after this check passes.
   This prevents anyone from faking a "successful" payment by just visiting
   the success URL.

## 6. Going live
Once you've tested with test keys and test cards/Mobile Money numbers, complete
Paystack's business verification (they'll ask for your Ghana Business Registration
or ID), then swap in your `pk_live_...` / `sk_live_...` keys.

## 7. Currency
Product prices in the database are stored as plain integers (no currency baked in).
All display templates now show `GH₵` instead of `$`. Paystack is charged in
**pesewas** (GHS × 100), which the payment view already handles for you.
