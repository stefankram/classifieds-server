class ItemRequest(models.Model):
    """
    Item Request Model

    A request made by a buyer to search for sellers that can sell the item they
    want

    """
    buyer_id = models.ForeignKey(
        db_column='buyer_id',
        on_delete=models.CASCADE,
        to=Buyer)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    description = models.TextField(
        db_column='description')

    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.CASCADE,
        to=Item)

    purchase_date = models.DateTimeField(
        db_column='purchase_date')