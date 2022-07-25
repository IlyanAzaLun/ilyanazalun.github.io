---
title: Ajax Request Datatabels
tags: [Ajax, Data Tabels]
style: 
color: 
description: Request to the server for each draw of the information on the page.
---

Source: [DataTables](https://datatables.net/manual/server-side#Example-data)

Processing in datatabels is enabled thought use of the `serverSide: true` option, and use
the `ajax: 'url'` :

## Example
### View
#### HTML in view
column in HTML must have on JQ request
```
<table id="example2" class="table table-sm table-bordered table-hover" style="font-size: 12px;">
  <thead>
    <tr>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> label </th>
      <th> OPTION </th>
    </tr>
  </thead>
</table>
```
#### REQUEST JQ in view
column on Request JQ must have on request controller
```
let tabel = $('#example').DataTabel({
	serverSide: true,
	ajax: {
        // if can using API to get this data.?
		'url' : "path/file/func",
        'type': "POST"
	},
    // Name Column
    columns: [{
      data: "id"
    },{
      data: "item_code",
    },{
      data: "item_name",
    },{
      data: "category"
    },{
      data: "brand"
    },{
      data: "brands"
    },{
      data: 'item_quantity',
    },{
      data: 'item_broken',
    },{
      data: 'weight',
    },{
      data: 'item_unit',
    },{
      data: "item_capital_price",
    },{
      data: "item_selling_price",
    },{
      data: "note"
    },

    // OPTION, U can customise return, use render function.. 
    {
      data: "id",
      orderable: false,
      render: function(data, type, row) {
        return `
            <div class="btn-group d-flex justify-content-center">
            <a target="_blank" href="<?= url('items') ?>/edit?id=${row['id']}" class="btn btn-xs btn-default" data-toggle="tooltip" data-placement="top" title="Edit items"><i class="fa fa-tw fa-edit text-primary"></i></a>
            <a target="_blank" href="<?= url('items') ?>/info?id=${row['item_code']}" class="btn btn-xs btn-default" data-toggle="tooltip" data-placement="top" title="History items"><i class="fa fa-tw fa-history text-primary"></i></a>
            <a target="_blank" href="<?= url('items') ?>/info_transaction?id=${row['item_code']}" class="btn btn-xs btn-default" data-toggle="tooltip" data-placement="top" title="History transaction items"><i class="fa fa-tw fa-layer-group text-primary"></i></a>
            <?php if(hasPermissions('list_fifo')):?>
            <a target="_blank" href="<?= url('items') ?>/info_fifo?id=${row['item_code']}" class="btn btn-xs btn-default" data-toggle="tooltip" data-placement="top" title="Fifo items"><i class="fa fa-tw fa-book text-primary"></i></a>
            <?php endif;?>
            </div>`;
      }
    },
  ]
})
```
### Controller Function Request
`$data[]` must have in column on selected on request table on database
```
function func(){
	$response = array();

    $postData = $this->input->post();

    ## Read value
    $draw = $postData['draw'];
    $start = $postData['start'];
    $rowperpage = $postData['length']; // Rows display per page
    $columnIndex = $postData['order'][0]['column']; // Column index
    $columnName = $postData['columns'][$columnIndex]['data']; // Column name
    $columnSortOrder = $postData['order'][0]['dir']; // asc or desc
    $searchValue = $postData['search']['value']; // Search value

    ## Total number of records without filtering
    $this->db->select('count(*) as allcount');
    $records = $this->db->get('items')->result();
    $totalRecords = $records[0]->allcount;

    ## Total number of record with filtering
    $this->db->select('count(*) as allcount');
    if ($searchValue != '') {
        // EXAMPLE //
        $this->db->like('item_name', $searchValue, 'both');
        $this->db->or_like('item_code', $searchValue, 'both');
        $this->db->or_like('category', $searchValue, 'both');
    }
    $records = $this->db->get('items')->result();
    $totalRecordwithFilter = $records[0]->allcount;

    ## Fetch records
    $this->db->select('*');
    if ($searchValue != '') {
        // EXAMPLE //
        $this->db->like('item_name', $searchValue, 'both');
        $this->db->or_like('item_code', $searchValue, 'both');
        $this->db->or_like('category', $searchValue, 'both');
    }
    $this->db->order_by($columnName, $columnSortOrder);
    $this->db->limit($rowperpage, $start);
    $records = $this->db->get('items')->result();

    $data = array();

    foreach ($records as $record) {

        $data[] = array(
            // EXAMPLE // Name Column
            "id" => $record->id,
            "item_code" => $record->item_code,
            "item_name" => $record->item_name,
            "category" => $record->category,
            "item_quantity" => $record->quantity,
            "item_broken" => $record->broken,
            "item_unit" => $record->unit,
            "item_capital_price" => $record->capital_price,
            "item_selling_price" => $record->selling_price,
            "note" => $record->note,
            "is_active" => $record->is_active,
        );
    }

    ## Response
    $response = array(
        "draw" => intval($draw),
        "iTotalRecords" => $totalRecords,
        "iTotalDisplayRecords" => $totalRecordwithFilter,
        "aaData" => $data
    );
    $this->output->set_content_type('application/json')->set_output(json_encode($response));
}
```

add event on datatabels draw,
```
tabel.on('draw', function(){
  // your function
})
```